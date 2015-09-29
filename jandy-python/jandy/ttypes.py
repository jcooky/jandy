#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ClassObject:
  """
  Attributes:
   - id
   - packageName
   - name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'packageName', None, None, ), # 2
    (3, TType.STRING, 'name', None, None, ), # 3
  )

  def __init__(self, id=None, packageName=None, name=None,):
    self.id = id
    self.packageName = packageName
    self.name = name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.packageName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ClassObject')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.packageName is not None:
      oprot.writeFieldBegin('packageName', TType.STRING, 2)
      oprot.writeString(self.packageName)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 3)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.packageName)
    value = (value * 31) ^ hash(self.name)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MethodObject:
  """
  Attributes:
   - id
   - name
   - access
   - descriptor
   - ownerId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'access', None, None, ), # 3
    (4, TType.STRING, 'descriptor', None, None, ), # 4
    (5, TType.STRING, 'ownerId', None, None, ), # 5
  )

  def __init__(self, id=None, name=None, access=None, descriptor=None, ownerId=None,):
    self.id = id
    self.name = name
    self.access = access
    self.descriptor = descriptor
    self.ownerId = ownerId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.access = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.descriptor = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.ownerId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MethodObject')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.access is not None:
      oprot.writeFieldBegin('access', TType.I32, 3)
      oprot.writeI32(self.access)
      oprot.writeFieldEnd()
    if self.descriptor is not None:
      oprot.writeFieldBegin('descriptor', TType.STRING, 4)
      oprot.writeString(self.descriptor)
      oprot.writeFieldEnd()
    if self.ownerId is not None:
      oprot.writeFieldBegin('ownerId', TType.STRING, 5)
      oprot.writeString(self.ownerId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.access)
    value = (value * 31) ^ hash(self.descriptor)
    value = (value * 31) ^ hash(self.ownerId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExceptionObject:
  """
  Attributes:
   - id
   - classId
   - casedById
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'classId', None, None, ), # 2
    (3, TType.STRING, 'casedById', None, None, ), # 3
    (4, TType.STRING, 'message', None, None, ), # 4
  )

  def __init__(self, id=None, classId=None, casedById=None, message=None,):
    self.id = id
    self.classId = classId
    self.casedById = casedById
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.classId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.casedById = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ExceptionObject')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.classId is not None:
      oprot.writeFieldBegin('classId', TType.STRING, 2)
      oprot.writeString(self.classId)
      oprot.writeFieldEnd()
    if self.casedById is not None:
      oprot.writeFieldBegin('casedById', TType.STRING, 3)
      oprot.writeString(self.casedById)
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 4)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.classId)
    value = (value * 31) ^ hash(self.casedById)
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Accumulator:
  """
  Attributes:
   - id
   - elapsedTime
   - startTime
   - concurThreadName
   - exceptionId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.I64, 'elapsedTime', None, None, ), # 2
    (3, TType.I64, 'startTime', None, None, ), # 3
    (4, TType.STRING, 'concurThreadName', None, None, ), # 4
    (5, TType.STRING, 'exceptionId', None, None, ), # 5
  )

  def __init__(self, id=None, elapsedTime=None, startTime=None, concurThreadName=None, exceptionId=None,):
    self.id = id
    self.elapsedTime = elapsedTime
    self.startTime = startTime
    self.concurThreadName = concurThreadName
    self.exceptionId = exceptionId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.elapsedTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.startTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.concurThreadName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.exceptionId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Accumulator')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.elapsedTime is not None:
      oprot.writeFieldBegin('elapsedTime', TType.I64, 2)
      oprot.writeI64(self.elapsedTime)
      oprot.writeFieldEnd()
    if self.startTime is not None:
      oprot.writeFieldBegin('startTime', TType.I64, 3)
      oprot.writeI64(self.startTime)
      oprot.writeFieldEnd()
    if self.concurThreadName is not None:
      oprot.writeFieldBegin('concurThreadName', TType.STRING, 4)
      oprot.writeString(self.concurThreadName)
      oprot.writeFieldEnd()
    if self.exceptionId is not None:
      oprot.writeFieldBegin('exceptionId', TType.STRING, 5)
      oprot.writeString(self.exceptionId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.elapsedTime)
    value = (value * 31) ^ hash(self.startTime)
    value = (value * 31) ^ hash(self.concurThreadName)
    value = (value * 31) ^ hash(self.exceptionId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TreeNode:
  """
  Attributes:
   - id
   - childrenIds
   - acc
   - methodId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.LIST, 'childrenIds', (TType.STRING,None), None, ), # 2
    (3, TType.STRUCT, 'acc', (Accumulator, Accumulator.thrift_spec), None, ), # 3
    (4, TType.STRING, 'methodId', None, None, ), # 4
  )

  def __init__(self, id=None, childrenIds=None, acc=None, methodId=None,):
    self.id = id
    self.childrenIds = childrenIds
    self.acc = acc
    self.methodId = methodId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.childrenIds = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.childrenIds.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.acc = Accumulator()
          self.acc.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.methodId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TreeNode')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.childrenIds is not None:
      oprot.writeFieldBegin('childrenIds', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.childrenIds))
      for iter6 in self.childrenIds:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.acc is not None:
      oprot.writeFieldBegin('acc', TType.STRUCT, 3)
      self.acc.write(oprot)
      oprot.writeFieldEnd()
    if self.methodId is not None:
      oprot.writeFieldBegin('methodId', TType.STRING, 4)
      oprot.writeString(self.methodId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.childrenIds)
    value = (value * 31) ^ hash(self.acc)
    value = (value * 31) ^ hash(self.methodId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ProfilingContext:
  """
  Attributes:
   - classes
   - methods
   - exceptions
   - nodes
   - root
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'classes', (TType.STRUCT,(ClassObject, ClassObject.thrift_spec)), None, ), # 1
    (2, TType.LIST, 'methods', (TType.STRUCT,(MethodObject, MethodObject.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'exceptions', (TType.STRUCT,(ExceptionObject, ExceptionObject.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'nodes', (TType.STRUCT,(TreeNode, TreeNode.thrift_spec)), None, ), # 4
    (5, TType.STRUCT, 'root', (TreeNode, TreeNode.thrift_spec), None, ), # 5
  )

  def __init__(self, classes=None, methods=None, exceptions=None, nodes=None, root=None,):
    self.classes = classes
    self.methods = methods
    self.exceptions = exceptions
    self.nodes = nodes
    self.root = root

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.classes = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = ClassObject()
            _elem12.read(iprot)
            self.classes.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.methods = []
          (_etype16, _size13) = iprot.readListBegin()
          for _i17 in xrange(_size13):
            _elem18 = MethodObject()
            _elem18.read(iprot)
            self.methods.append(_elem18)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.exceptions = []
          (_etype22, _size19) = iprot.readListBegin()
          for _i23 in xrange(_size19):
            _elem24 = ExceptionObject()
            _elem24.read(iprot)
            self.exceptions.append(_elem24)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.nodes = []
          (_etype28, _size25) = iprot.readListBegin()
          for _i29 in xrange(_size25):
            _elem30 = TreeNode()
            _elem30.read(iprot)
            self.nodes.append(_elem30)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.root = TreeNode()
          self.root.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ProfilingContext')
    if self.classes is not None:
      oprot.writeFieldBegin('classes', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.classes))
      for iter31 in self.classes:
        iter31.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.methods is not None:
      oprot.writeFieldBegin('methods', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.methods))
      for iter32 in self.methods:
        iter32.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.exceptions is not None:
      oprot.writeFieldBegin('exceptions', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.exceptions))
      for iter33 in self.exceptions:
        iter33.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.nodes is not None:
      oprot.writeFieldBegin('nodes', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.nodes))
      for iter34 in self.nodes:
        iter34.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.root is not None:
      oprot.writeFieldBegin('root', TType.STRUCT, 5)
      self.root.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.classes)
    value = (value * 31) ^ hash(self.methods)
    value = (value * 31) ^ hash(self.exceptions)
    value = (value * 31) ^ hash(self.nodes)
    value = (value * 31) ^ hash(self.root)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)