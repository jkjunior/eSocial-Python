#!/usr/bin/env python

#
# Generated Wed Oct 10 14:18:14 2018 by generateDS.py version 2.29.24.
# Python 3.6.5 (default, May 11 2018, 13:30:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'classes/evtCS.py')
#   ('-s', 'classes/evtCSSub.py')
#   ('--super', 'evtCS')
#
# Command line arguments:
#   /home/joao/Documents/teste_xsd/xsd/evtCS.xsd
#
# Command line:
#   /home/joao/Documents/teste_xsd/dkuhlman-generateds-60c208fd6e8d/generateDS.py -o "classes/evtCS.py" -s "classes/evtCSSub.py" --super="evtCS" /home/joao/Documents/teste_xsd/xsd/evtCS.xsd
#
# Current working directory (os.getcwd()):
#   teste_xsd
#

import sys
from lxml import etree as etree_

import evtCS as supermod

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
    def __init__(self, evtCS=None, Signature=None):
        super(eSocialSub, self).__init__(evtCS, Signature, )
supermod.eSocial.subclass = eSocialSub
# end class eSocialSub


class TEmpregadorSub(supermod.TEmpregador):
    def __init__(self, tpInsc=None, nrInsc=None):
        super(TEmpregadorSub, self).__init__(tpInsc, nrInsc, )
supermod.TEmpregador.subclass = TEmpregadorSub
# end class TEmpregadorSub


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


class evtCSTypeSub(supermod.evtCSType):
    def __init__(self, Id=None, ideEvento=None, ideEmpregador=None, infoCS=None):
        super(evtCSTypeSub, self).__init__(Id, ideEvento, ideEmpregador, infoCS, )
supermod.evtCSType.subclass = evtCSTypeSub
# end class evtCSTypeSub


class ideEventoTypeSub(supermod.ideEventoType):
    def __init__(self, indApuracao=None, perApur=None):
        super(ideEventoTypeSub, self).__init__(indApuracao, perApur, )
supermod.ideEventoType.subclass = ideEventoTypeSub
# end class ideEventoTypeSub


class infoCSTypeSub(supermod.infoCSType):
    def __init__(self, nrRecArqBase=None, indExistInfo=None, infoCPSeg=None, infoContrib=None, ideEstab=None, infoCRContrib=None):
        super(infoCSTypeSub, self).__init__(nrRecArqBase, indExistInfo, infoCPSeg, infoContrib, ideEstab, infoCRContrib, )
supermod.infoCSType.subclass = infoCSTypeSub
# end class infoCSTypeSub


class infoCPSegTypeSub(supermod.infoCPSegType):
    def __init__(self, vrDescCP=None, vrCpSeg=None):
        super(infoCPSegTypeSub, self).__init__(vrDescCP, vrCpSeg, )
supermod.infoCPSegType.subclass = infoCPSegTypeSub
# end class infoCPSegTypeSub


class infoContribTypeSub(supermod.infoContribType):
    def __init__(self, classTrib=None, infoPJ=None):
        super(infoContribTypeSub, self).__init__(classTrib, infoPJ, )
supermod.infoContribType.subclass = infoContribTypeSub
# end class infoContribTypeSub


class infoPJTypeSub(supermod.infoPJType):
    def __init__(self, indCoop=None, indConstr=None, indSubstPatr=None, percRedContrib=None, infoAtConc=None):
        super(infoPJTypeSub, self).__init__(indCoop, indConstr, indSubstPatr, percRedContrib, infoAtConc, )
supermod.infoPJType.subclass = infoPJTypeSub
# end class infoPJTypeSub


class infoAtConcTypeSub(supermod.infoAtConcType):
    def __init__(self, fatorMes=None, fator13=None):
        super(infoAtConcTypeSub, self).__init__(fatorMes, fator13, )
supermod.infoAtConcType.subclass = infoAtConcTypeSub
# end class infoAtConcTypeSub


class ideEstabTypeSub(supermod.ideEstabType):
    def __init__(self, tpInsc=None, nrInsc=None, infoEstab=None, ideLotacao=None, basesAquis=None, basesComerc=None, infoCREstab=None):
        super(ideEstabTypeSub, self).__init__(tpInsc, nrInsc, infoEstab, ideLotacao, basesAquis, basesComerc, infoCREstab, )
supermod.ideEstabType.subclass = ideEstabTypeSub
# end class ideEstabTypeSub


class infoEstabTypeSub(supermod.infoEstabType):
    def __init__(self, cnaePrep=None, aliqRat=None, fap=None, aliqRatAjust=None, infoComplObra=None):
        super(infoEstabTypeSub, self).__init__(cnaePrep, aliqRat, fap, aliqRatAjust, infoComplObra, )
supermod.infoEstabType.subclass = infoEstabTypeSub
# end class infoEstabTypeSub


class infoComplObraTypeSub(supermod.infoComplObraType):
    def __init__(self, indSubstPatrObra=None):
        super(infoComplObraTypeSub, self).__init__(indSubstPatrObra, )
supermod.infoComplObraType.subclass = infoComplObraTypeSub
# end class infoComplObraTypeSub


class ideLotacaoTypeSub(supermod.ideLotacaoType):
    def __init__(self, codLotacao=None, fpas=None, codTercs=None, codTercsSusp=None, infoTercSusp=None, infoEmprParcial=None, dadosOpPort=None, basesRemun=None, basesAvNPort=None, infoSubstPatrOpPort=None):
        super(ideLotacaoTypeSub, self).__init__(codLotacao, fpas, codTercs, codTercsSusp, infoTercSusp, infoEmprParcial, dadosOpPort, basesRemun, basesAvNPort, infoSubstPatrOpPort, )
supermod.ideLotacaoType.subclass = ideLotacaoTypeSub
# end class ideLotacaoTypeSub


class infoTercSuspTypeSub(supermod.infoTercSuspType):
    def __init__(self, codTerc=None):
        super(infoTercSuspTypeSub, self).__init__(codTerc, )
supermod.infoTercSuspType.subclass = infoTercSuspTypeSub
# end class infoTercSuspTypeSub


class infoEmprParcialTypeSub(supermod.infoEmprParcialType):
    def __init__(self, tpInscContrat=None, nrInscContrat=None, tpInscProp=None, nrInscProp=None):
        super(infoEmprParcialTypeSub, self).__init__(tpInscContrat, nrInscContrat, tpInscProp, nrInscProp, )
supermod.infoEmprParcialType.subclass = infoEmprParcialTypeSub
# end class infoEmprParcialTypeSub


class dadosOpPortTypeSub(supermod.dadosOpPortType):
    def __init__(self, cnpjOpPortuario=None, aliqRat=None, fap=None, aliqRatAjust=None):
        super(dadosOpPortTypeSub, self).__init__(cnpjOpPortuario, aliqRat, fap, aliqRatAjust, )
supermod.dadosOpPortType.subclass = dadosOpPortTypeSub
# end class dadosOpPortTypeSub


class basesRemunTypeSub(supermod.basesRemunType):
    def __init__(self, indIncid=None, codCateg=None, basesCp=None):
        super(basesRemunTypeSub, self).__init__(indIncid, codCateg, basesCp, )
supermod.basesRemunType.subclass = basesRemunTypeSub
# end class basesRemunTypeSub


class basesCpTypeSub(supermod.basesCpType):
    def __init__(self, vrBcCp00=None, vrBcCp15=None, vrBcCp20=None, vrBcCp25=None, vrSuspBcCp00=None, vrSuspBcCp15=None, vrSuspBcCp20=None, vrSuspBcCp25=None, vrDescSest=None, vrCalcSest=None, vrDescSenat=None, vrCalcSenat=None, vrSalFam=None, vrSalMat=None):
        super(basesCpTypeSub, self).__init__(vrBcCp00, vrBcCp15, vrBcCp20, vrBcCp25, vrSuspBcCp00, vrSuspBcCp15, vrSuspBcCp20, vrSuspBcCp25, vrDescSest, vrCalcSest, vrDescSenat, vrCalcSenat, vrSalFam, vrSalMat, )
supermod.basesCpType.subclass = basesCpTypeSub
# end class basesCpTypeSub


class basesAvNPortTypeSub(supermod.basesAvNPortType):
    def __init__(self, vrBcCp00=None, vrBcCp15=None, vrBcCp20=None, vrBcCp25=None, vrBcCp13=None, vrBcFgts=None, vrDescCP=None):
        super(basesAvNPortTypeSub, self).__init__(vrBcCp00, vrBcCp15, vrBcCp20, vrBcCp25, vrBcCp13, vrBcFgts, vrDescCP, )
supermod.basesAvNPortType.subclass = basesAvNPortTypeSub
# end class basesAvNPortTypeSub


class infoSubstPatrOpPortTypeSub(supermod.infoSubstPatrOpPortType):
    def __init__(self, cnpjOpPortuario=None):
        super(infoSubstPatrOpPortTypeSub, self).__init__(cnpjOpPortuario, )
supermod.infoSubstPatrOpPortType.subclass = infoSubstPatrOpPortTypeSub
# end class infoSubstPatrOpPortTypeSub


class basesAquisTypeSub(supermod.basesAquisType):
    def __init__(self, indAquis=None, vlrAquis=None, vrCPDescPR=None, vrCPNRet=None, vrRatNRet=None, vrSenarNRet=None, vrCPCalcPR=None, vrRatDescPR=None, vrRatCalcPR=None, vrSenarDesc=None, vrSenarCalc=None):
        super(basesAquisTypeSub, self).__init__(indAquis, vlrAquis, vrCPDescPR, vrCPNRet, vrRatNRet, vrSenarNRet, vrCPCalcPR, vrRatDescPR, vrRatCalcPR, vrSenarDesc, vrSenarCalc, )
supermod.basesAquisType.subclass = basesAquisTypeSub
# end class basesAquisTypeSub


class basesComercTypeSub(supermod.basesComercType):
    def __init__(self, indComerc=None, vrBcComPR=None, vrCPSusp=None, vrRatSusp=None, vrSenarSusp=None):
        super(basesComercTypeSub, self).__init__(indComerc, vrBcComPR, vrCPSusp, vrRatSusp, vrSenarSusp, )
supermod.basesComercType.subclass = basesComercTypeSub
# end class basesComercTypeSub


class infoCREstabTypeSub(supermod.infoCREstabType):
    def __init__(self, tpCR=None, vrCR=None, vrSuspCR=None):
        super(infoCREstabTypeSub, self).__init__(tpCR, vrCR, vrSuspCR, )
supermod.infoCREstabType.subclass = infoCREstabTypeSub
# end class infoCREstabTypeSub


class infoCRContribTypeSub(supermod.infoCRContribType):
    def __init__(self, tpCR=None, vrCR=None, vrCRSusp=None):
        super(infoCRContribTypeSub, self).__init__(tpCR, vrCR, vrCRSusp, )
supermod.infoCRContribType.subclass = infoCRContribTypeSub
# end class infoCRContribTypeSub


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
        sys.stdout.write('#from evtCS import *\n\n')
        sys.stdout.write('import evtCS as model_\n\n')
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
