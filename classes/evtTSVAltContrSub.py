#!/usr/bin/env python

#
# Generated Wed Oct 10 14:18:15 2018 by generateDS.py version 2.29.24.
# Python 3.6.5 (default, May 11 2018, 13:30:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'classes/evtTSVAltContr.py')
#   ('-s', 'classes/evtTSVAltContrSub.py')
#   ('--super', 'evtTSVAltContr')
#
# Command line arguments:
#   /home/joao/Documents/teste_xsd/xsd/evtTSVAltContr.xsd
#
# Command line:
#   /home/joao/Documents/teste_xsd/dkuhlman-generateds-60c208fd6e8d/generateDS.py -o "classes/evtTSVAltContr.py" -s "classes/evtTSVAltContrSub.py" --super="evtTSVAltContr" /home/joao/Documents/teste_xsd/xsd/evtTSVAltContr.xsd
#
# Current working directory (os.getcwd()):
#   teste_xsd
#

import sys
from lxml import etree as etree_

import evtTSVAltContr as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class eSocialSub(supermod.eSocial):
    def __init__(self, evtTSVAltContr=None, Signature=None):
        super(eSocialSub, self).__init__(evtTSVAltContr, Signature, )
supermod.eSocial.subclass = eSocialSub
# end class eSocialSub


class TIdeEveTrabSub(supermod.TIdeEveTrab):
    def __init__(self, indRetif=None, nrRecibo=None, tpAmb=None, procEmi=None, verProc=None):
        super(TIdeEveTrabSub, self).__init__(indRetif, nrRecibo, tpAmb, procEmi, verProc, )
supermod.TIdeEveTrab.subclass = TIdeEveTrabSub
# end class TIdeEveTrabSub


class TEmpregadorSub(supermod.TEmpregador):
    def __init__(self, tpInsc=None, nrInsc=None):
        super(TEmpregadorSub, self).__init__(tpInsc, nrInsc, )
supermod.TEmpregador.subclass = TEmpregadorSub
# end class TEmpregadorSub


class TRemunSub(supermod.TRemun):
    def __init__(self, vrSalFx=None, undSalFixo=None, dscSalVar=None):
        super(TRemunSub, self).__init__(vrSalFx, undSalFixo, dscSalVar, )
supermod.TRemun.subclass = TRemunSub
# end class TRemunSub


class SignatureTypeSub(supermod.SignatureType):
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None):
        super(SignatureTypeSub, self).__init__(Id, SignedInfo, SignatureValue, KeyInfo, Object, )
supermod.SignatureType.subclass = SignatureTypeSub
# end class SignatureTypeSub


class SignatureValueTypeSub(supermod.SignatureValueType):
    def __init__(self, Id=None, valueOf_=None):
        super(SignatureValueTypeSub, self).__init__(Id, valueOf_, )
supermod.SignatureValueType.subclass = SignatureValueTypeSub
# end class SignatureValueTypeSub


class SignedInfoTypeSub(supermod.SignedInfoType):
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None):
        super(SignedInfoTypeSub, self).__init__(Id, CanonicalizationMethod, SignatureMethod, Reference, )
supermod.SignedInfoType.subclass = SignedInfoTypeSub
# end class SignedInfoTypeSub


class CanonicalizationMethodTypeSub(supermod.CanonicalizationMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(CanonicalizationMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.CanonicalizationMethodType.subclass = CanonicalizationMethodTypeSub
# end class CanonicalizationMethodTypeSub


class SignatureMethodTypeSub(supermod.SignatureMethodType):
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignatureMethodTypeSub, self).__init__(Algorithm, HMACOutputLength, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignatureMethodType.subclass = SignatureMethodTypeSub
# end class SignatureMethodTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None):
        super(ReferenceTypeSub, self).__init__(Id, URI, Type, Transforms, DigestMethod, DigestValue, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class TransformsTypeSub(supermod.TransformsType):
    def __init__(self, Transform=None):
        super(TransformsTypeSub, self).__init__(Transform, )
supermod.TransformsType.subclass = TransformsTypeSub
# end class TransformsTypeSub


class TransformTypeSub(supermod.TransformType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None):
        super(TransformTypeSub, self).__init__(Algorithm, anytypeobjs_, XPath, valueOf_, mixedclass_, content_, )
supermod.TransformType.subclass = TransformTypeSub
# end class TransformTypeSub


class DigestMethodTypeSub(supermod.DigestMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(DigestMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.DigestMethodType.subclass = DigestMethodTypeSub
# end class DigestMethodTypeSub


class KeyInfoTypeSub(supermod.KeyInfoType):
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyInfoTypeSub, self).__init__(Id, KeyName, KeyValue, RetrievalMethod, X509Data, PGPData, SPKIData, MgmtData, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyInfoType.subclass = KeyInfoTypeSub
# end class KeyInfoTypeSub


class KeyValueTypeSub(supermod.KeyValueType):
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyValueTypeSub, self).__init__(DSAKeyValue, RSAKeyValue, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyValueType.subclass = KeyValueTypeSub
# end class KeyValueTypeSub


class RetrievalMethodTypeSub(supermod.RetrievalMethodType):
    def __init__(self, URI=None, Type=None, Transforms=None):
        super(RetrievalMethodTypeSub, self).__init__(URI, Type, Transforms, )
supermod.RetrievalMethodType.subclass = RetrievalMethodTypeSub
# end class RetrievalMethodTypeSub


class X509DataTypeSub(supermod.X509DataType):
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None):
        super(X509DataTypeSub, self).__init__(X509IssuerSerial, X509SKI, X509SubjectName, X509Certificate, X509CRL, anytypeobjs_, )
supermod.X509DataType.subclass = X509DataTypeSub
# end class X509DataTypeSub


class X509IssuerSerialTypeSub(supermod.X509IssuerSerialType):
    def __init__(self, X509IssuerName=None, X509SerialNumber=None):
        super(X509IssuerSerialTypeSub, self).__init__(X509IssuerName, X509SerialNumber, )
supermod.X509IssuerSerialType.subclass = X509IssuerSerialTypeSub
# end class X509IssuerSerialTypeSub


class PGPDataTypeSub(supermod.PGPDataType):
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None):
        super(PGPDataTypeSub, self).__init__(PGPKeyID, PGPKeyPacket, anytypeobjs_, )
supermod.PGPDataType.subclass = PGPDataTypeSub
# end class PGPDataTypeSub


class SPKIDataTypeSub(supermod.SPKIDataType):
    def __init__(self, SPKISexp=None, anytypeobjs_=None):
        super(SPKIDataTypeSub, self).__init__(SPKISexp, anytypeobjs_, )
supermod.SPKIDataType.subclass = SPKIDataTypeSub
# end class SPKIDataTypeSub


class ObjectTypeSub(supermod.ObjectType):
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(ObjectTypeSub, self).__init__(Id, MimeType, Encoding, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.ObjectType.subclass = ObjectTypeSub
# end class ObjectTypeSub


class ManifestTypeSub(supermod.ManifestType):
    def __init__(self, Id=None, Reference=None):
        super(ManifestTypeSub, self).__init__(Id, Reference, )
supermod.ManifestType.subclass = ManifestTypeSub
# end class ManifestTypeSub


class SignaturePropertiesTypeSub(supermod.SignaturePropertiesType):
    def __init__(self, Id=None, SignatureProperty=None):
        super(SignaturePropertiesTypeSub, self).__init__(Id, SignatureProperty, )
supermod.SignaturePropertiesType.subclass = SignaturePropertiesTypeSub
# end class SignaturePropertiesTypeSub


class SignaturePropertyTypeSub(supermod.SignaturePropertyType):
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignaturePropertyTypeSub, self).__init__(Target, Id, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignaturePropertyType.subclass = SignaturePropertyTypeSub
# end class SignaturePropertyTypeSub


class DSAKeyValueTypeSub(supermod.DSAKeyValueType):
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None):
        super(DSAKeyValueTypeSub, self).__init__(P, Q, G, Y, J, Seed, PgenCounter, )
supermod.DSAKeyValueType.subclass = DSAKeyValueTypeSub
# end class DSAKeyValueTypeSub


class RSAKeyValueTypeSub(supermod.RSAKeyValueType):
    def __init__(self, Modulus=None, Exponent=None):
        super(RSAKeyValueTypeSub, self).__init__(Modulus, Exponent, )
supermod.RSAKeyValueType.subclass = RSAKeyValueTypeSub
# end class RSAKeyValueTypeSub


class evtTSVAltContrTypeSub(supermod.evtTSVAltContrType):
    def __init__(self, Id=None, ideEvento=None, ideEmpregador=None, ideTrabSemVinculo=None, infoTSVAlteracao=None):
        super(evtTSVAltContrTypeSub, self).__init__(Id, ideEvento, ideEmpregador, ideTrabSemVinculo, infoTSVAlteracao, )
supermod.evtTSVAltContrType.subclass = evtTSVAltContrTypeSub
# end class evtTSVAltContrTypeSub


class ideTrabSemVinculoTypeSub(supermod.ideTrabSemVinculoType):
    def __init__(self, cpfTrab=None, nisTrab=None, codCateg=None):
        super(ideTrabSemVinculoTypeSub, self).__init__(cpfTrab, nisTrab, codCateg, )
supermod.ideTrabSemVinculoType.subclass = ideTrabSemVinculoTypeSub
# end class ideTrabSemVinculoTypeSub


class infoTSVAlteracaoTypeSub(supermod.infoTSVAlteracaoType):
    def __init__(self, dtAlteracao=None, natAtividade=None, infoComplementares=None):
        super(infoTSVAlteracaoTypeSub, self).__init__(dtAlteracao, natAtividade, infoComplementares, )
supermod.infoTSVAlteracaoType.subclass = infoTSVAlteracaoTypeSub
# end class infoTSVAlteracaoTypeSub


class infoComplementaresTypeSub(supermod.infoComplementaresType):
    def __init__(self, cargoFuncao=None, remuneracao=None, infoEstagiario=None):
        super(infoComplementaresTypeSub, self).__init__(cargoFuncao, remuneracao, infoEstagiario, )
supermod.infoComplementaresType.subclass = infoComplementaresTypeSub
# end class infoComplementaresTypeSub


class cargoFuncaoTypeSub(supermod.cargoFuncaoType):
    def __init__(self, codCargo=None, codFuncao=None):
        super(cargoFuncaoTypeSub, self).__init__(codCargo, codFuncao, )
supermod.cargoFuncaoType.subclass = cargoFuncaoTypeSub
# end class cargoFuncaoTypeSub


class infoEstagiarioTypeSub(supermod.infoEstagiarioType):
    def __init__(self, natEstagio=None, nivEstagio=None, areaAtuacao=None, nrApol=None, vlrBolsa=None, dtPrevTerm=None, instEnsino=None, ageIntegracao=None, supervisorEstagio=None):
        super(infoEstagiarioTypeSub, self).__init__(natEstagio, nivEstagio, areaAtuacao, nrApol, vlrBolsa, dtPrevTerm, instEnsino, ageIntegracao, supervisorEstagio, )
supermod.infoEstagiarioType.subclass = infoEstagiarioTypeSub
# end class infoEstagiarioTypeSub


class instEnsinoTypeSub(supermod.instEnsinoType):
    def __init__(self, cnpjInstEnsino=None, nmRazao=None, dscLograd=None, nrLograd=None, bairro=None, cep=None, codMunic=None, uf=None):
        super(instEnsinoTypeSub, self).__init__(cnpjInstEnsino, nmRazao, dscLograd, nrLograd, bairro, cep, codMunic, uf, )
supermod.instEnsinoType.subclass = instEnsinoTypeSub
# end class instEnsinoTypeSub


class ageIntegracaoTypeSub(supermod.ageIntegracaoType):
    def __init__(self, cnpjAgntInteg=None, nmRazao=None, dscLograd=None, nrLograd=None, bairro=None, cep=None, codMunic=None, uf=None):
        super(ageIntegracaoTypeSub, self).__init__(cnpjAgntInteg, nmRazao, dscLograd, nrLograd, bairro, cep, codMunic, uf, )
supermod.ageIntegracaoType.subclass = ageIntegracaoTypeSub
# end class ageIntegracaoTypeSub


class supervisorEstagioTypeSub(supermod.supervisorEstagioType):
    def __init__(self, cpfSupervisor=None, nmSuperv=None):
        super(supervisorEstagioTypeSub, self).__init__(cpfSupervisor, nmSuperv, )
supermod.supervisorEstagioType.subclass = supervisorEstagioTypeSub
# end class supervisorEstagioTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from evtTSVAltContr import *\n\n')
        sys.stdout.write('import evtTSVAltContr as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
