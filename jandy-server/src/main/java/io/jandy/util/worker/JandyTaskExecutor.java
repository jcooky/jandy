package io.jandy.util.worker;

/**
 * Created by jcooky on 2017. 3. 28..
 */
public interface JandyTaskExecutor {
    void execute(JandyTask task, JandyTaskExecutionContext context);
}
