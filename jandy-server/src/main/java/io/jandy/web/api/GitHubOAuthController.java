package io.jandy.web.api;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import lombok.val;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import javax.annotation.PostConstruct;
import java.util.Map;

/**
 * GitHubOAuthController
 *
 * @author jcooky
 * @since 2018. 6. 8.
 */
@RestController
@RequestMapping("/rest/github/oauth")
@Slf4j
public class GitHubOAuthController {
    @Autowired
    private Environment env;

    private String clientId, clientSecret;
    private RestTemplate restTemplate = new RestTemplate();

    @PostMapping("/access-token")
    public ResponseEntity<AccessTokenResult> getAccessToken(@RequestBody Map<String, String> body) {
        body.put("client_id", clientId);
        body.put("client_secret", clientSecret);

        val headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        headers.add(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON_VALUE);

        val response = restTemplate.exchange(
                "https://github.com/login/oauth/access_token",
                HttpMethod.POST,
                new HttpEntity<>(body, headers),
                AccessTokenResult.class
        );

        return ResponseEntity.status(response.getStatusCode())
                .body(response.getBody());
    }

    @PostConstruct
    public void init() {
        this.clientId = env.getProperty("security.oauth2.client.clientId");
        this.clientSecret = env.getProperty("security.oauth2.client.clientSecret");
    }

    @Data
    private static class AccessTokenResult {
        @JsonProperty("access_token")
        private String accessToken;

        @JsonProperty("token_type")
        private String tokenType;
    }
}
