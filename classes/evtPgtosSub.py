#!/usr/bin/env python

#
# Generated Wed Oct 10 14:18:15 2018 by generateDS.py version 2.29.24.
# Python 3.6.5 (default, May 11 2018, 13:30:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'classes/evtPgtos.py')
#   ('-s', 'classes/evtPgtosSub.py')
#   ('--super', 'evtPgtos')
#
# Command line arguments:
#   /home/joao/Documents/teste_xsd/xsd/evtPgtos.xsd
#
# Command line:
#   /home/joao/Documents/teste_xsd/dkuhlman-generateds-60c208fd6e8d/generateDS.py -o "classes/evtPgtos.py" -s "classes/evtPgtosSub.py" --super="evtPgtos" /home/joao/Documents/teste_xsd/xsd/evtPgtos.xsd
#
# Current working directory (os.getcwd()):
#   teste_xsd
#

import sys
from lxml import etree as etree_

import evtPgtos as supermod

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
    def __init__(self, evtPgtos=None, Signature=None):
        super(eSocialSub, self).__init__(evtPgtos, Signature, )
supermod.eSocial.subclass = eSocialSub
# end class eSocialSub


class TIdeEveFopagMensalSub(supermod.TIdeEveFopagMensal):
    def __init__(self, indRetif=None, nrRecibo=None, indApuracao=None, perApur=None, tpAmb=None, procEmi=None, verProc=None):
        super(TIdeEveFopagMensalSub, self).__init__(indRetif, nrRecibo, indApuracao, perApur, tpAmb, procEmi, verProc, )
supermod.TIdeEveFopagMensal.subclass = TIdeEveFopagMensalSub
# end class TIdeEveFopagMensalSub


class TEmpregadorSub(supermod.TEmpregador):
    def __init__(self, tpInsc=None, nrInsc=None):
        super(TEmpregadorSub, self).__init__(tpInsc, nrInsc, )
supermod.TEmpregador.subclass = TEmpregadorSub
# end class TEmpregadorSub


class TPensaoAlimSub(supermod.TPensaoAlim):
    def __init__(self, cpfBenef=None, dtNasctoBenef=None, nmBenefic=None, vlrPensao=None):
        super(TPensaoAlimSub, self).__init__(cpfBenef, dtNasctoBenef, nmBenefic, vlrPensao, )
supermod.TPensaoAlim.subclass = TPensaoAlimSub
# end class TPensaoAlimSub


class TRubrCaixaSub(supermod.TRubrCaixa):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None):
        super(TRubrCaixaSub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, )
supermod.TRubrCaixa.subclass = TRubrCaixaSub
# end class TRubrCaixaSub


class TNaoResidSub(supermod.TNaoResid):
    def __init__(self, idePais=None, endExt=None):
        super(TNaoResidSub, self).__init__(idePais, endExt, )
supermod.TNaoResid.subclass = TNaoResidSub
# end class TNaoResidSub


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


class evtPgtosTypeSub(supermod.evtPgtosType):
    def __init__(self, Id=None, ideEvento=None, ideEmpregador=None, ideBenef=None):
        super(evtPgtosTypeSub, self).__init__(Id, ideEvento, ideEmpregador, ideBenef, )
supermod.evtPgtosType.subclass = evtPgtosTypeSub
# end class evtPgtosTypeSub


class ideBenefTypeSub(supermod.ideBenefType):
    def __init__(self, cpfBenef=None, deps=None, infoPgto=None):
        super(ideBenefTypeSub, self).__init__(cpfBenef, deps, infoPgto, )
supermod.ideBenefType.subclass = ideBenefTypeSub
# end class ideBenefTypeSub


class depsTypeSub(supermod.depsType):
    def __init__(self, vrDedDep=None):
        super(depsTypeSub, self).__init__(vrDedDep, )
supermod.depsType.subclass = depsTypeSub
# end class depsTypeSub


class infoPgtoTypeSub(supermod.infoPgtoType):
    def __init__(self, dtPgto=None, tpPgto=None, indResBr=None, detPgtoFl=None, detPgtoBenPr=None, detPgtoFer=None, detPgtoAnt=None, idePgtoExt=None):
        super(infoPgtoTypeSub, self).__init__(dtPgto, tpPgto, indResBr, detPgtoFl, detPgtoBenPr, detPgtoFer, detPgtoAnt, idePgtoExt, )
supermod.infoPgtoType.subclass = infoPgtoTypeSub
# end class infoPgtoTypeSub


class detPgtoFlTypeSub(supermod.detPgtoFlType):
    def __init__(self, perRef=None, ideDmDev=None, indPgtoTt=None, vrLiq=None, nrRecArq=None, retPgtoTot=None, infoPgtoParc=None):
        super(detPgtoFlTypeSub, self).__init__(perRef, ideDmDev, indPgtoTt, vrLiq, nrRecArq, retPgtoTot, infoPgtoParc, )
supermod.detPgtoFlType.subclass = detPgtoFlTypeSub
# end class detPgtoFlTypeSub


class retPgtoTotTypeSub(supermod.retPgtoTotType):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None, penAlim=None):
        super(retPgtoTotTypeSub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, penAlim, )
supermod.retPgtoTotType.subclass = retPgtoTotTypeSub
# end class retPgtoTotTypeSub


class infoPgtoParcTypeSub(supermod.infoPgtoParcType):
    def __init__(self, matricula=None, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None):
        super(infoPgtoParcTypeSub, self).__init__(matricula, codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, )
supermod.infoPgtoParcType.subclass = infoPgtoParcTypeSub
# end class infoPgtoParcTypeSub


class detPgtoBenPrTypeSub(supermod.detPgtoBenPrType):
    def __init__(self, perRef=None, ideDmDev=None, indPgtoTt=None, vrLiq=None, retPgtoTot=None, infoPgtoParc=None):
        super(detPgtoBenPrTypeSub, self).__init__(perRef, ideDmDev, indPgtoTt, vrLiq, retPgtoTot, infoPgtoParc, )
supermod.detPgtoBenPrType.subclass = detPgtoBenPrTypeSub
# end class detPgtoBenPrTypeSub


class infoPgtoParcType11Sub(supermod.infoPgtoParcType11):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None):
        super(infoPgtoParcType11Sub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, )
supermod.infoPgtoParcType11.subclass = infoPgtoParcType11Sub
# end class infoPgtoParcType11Sub


class detPgtoFerTypeSub(supermod.detPgtoFerType):
    def __init__(self, codCateg=None, matricula=None, dtIniGoz=None, qtDias=None, vrLiq=None, detRubrFer=None):
        super(detPgtoFerTypeSub, self).__init__(codCateg, matricula, dtIniGoz, qtDias, vrLiq, detRubrFer, )
supermod.detPgtoFerType.subclass = detPgtoFerTypeSub
# end class detPgtoFerTypeSub


class detRubrFerTypeSub(supermod.detRubrFerType):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None, penAlim=None):
        super(detRubrFerTypeSub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, penAlim, )
supermod.detRubrFerType.subclass = detRubrFerTypeSub
# end class detRubrFerTypeSub


class detPgtoAntTypeSub(supermod.detPgtoAntType):
    def __init__(self, codCateg=None, infoPgtoAnt=None):
        super(detPgtoAntTypeSub, self).__init__(codCateg, infoPgtoAnt, )
supermod.detPgtoAntType.subclass = detPgtoAntTypeSub
# end class detPgtoAntTypeSub


class infoPgtoAntTypeSub(supermod.infoPgtoAntType):
    def __init__(self, tpBcIRRF=None, vrBcIRRF=None):
        super(infoPgtoAntTypeSub, self).__init__(tpBcIRRF, vrBcIRRF, )
supermod.infoPgtoAntType.subclass = infoPgtoAntTypeSub
# end class infoPgtoAntTypeSub


class idePaisTypeSub(supermod.idePaisType):
    def __init__(self, codPais=None, indNIF=None, nifBenef=None):
        super(idePaisTypeSub, self).__init__(codPais, indNIF, nifBenef, )
supermod.idePaisType.subclass = idePaisTypeSub
# end class idePaisTypeSub


class endExtTypeSub(supermod.endExtType):
    def __init__(self, dscLograd=None, nrLograd=None, complem=None, bairro=None, nmCid=None, codPostal=None):
        super(endExtTypeSub, self).__init__(dscLograd, nrLograd, complem, bairro, nmCid, codPostal, )
supermod.endExtType.subclass = endExtTypeSub
# end class endExtTypeSub


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
        sys.stdout.write('#from evtPgtos import *\n\n')
        sys.stdout.write('import evtPgtos as model_\n\n')
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
