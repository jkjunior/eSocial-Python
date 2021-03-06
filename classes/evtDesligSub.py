#!/usr/bin/env python

#
# Generated Wed Oct 10 14:18:11 2018 by generateDS.py version 2.29.24.
# Python 3.6.5 (default, May 11 2018, 13:30:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'classes/evtDeslig.py')
#   ('-s', 'classes/evtDesligSub.py')
#   ('--super', 'evtDeslig')
#
# Command line arguments:
#   /home/joao/Documents/teste_xsd/xsd/evtDeslig.xsd
#
# Command line:
#   /home/joao/Documents/teste_xsd/dkuhlman-generateds-60c208fd6e8d/generateDS.py -o "classes/evtDeslig.py" -s "classes/evtDesligSub.py" --super="evtDeslig" /home/joao/Documents/teste_xsd/xsd/evtDeslig.xsd
#
# Current working directory (os.getcwd()):
#   teste_xsd
#

import sys
from lxml import etree as etree_

import evtDeslig as supermod

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
    def __init__(self, evtDeslig=None, Signature=None):
        super(eSocialSub, self).__init__(evtDeslig, Signature, )
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


class TIdeVinculoNisObrigSub(supermod.TIdeVinculoNisObrig):
    def __init__(self, cpfTrab=None, nisTrab=None, matricula=None):
        super(TIdeVinculoNisObrigSub, self).__init__(cpfTrab, nisTrab, matricula, )
supermod.TIdeVinculoNisObrig.subclass = TIdeVinculoNisObrigSub
# end class TIdeVinculoNisObrigSub


class TSaudeColSub(supermod.TSaudeCol):
    def __init__(self, detOper=None):
        super(TSaudeColSub, self).__init__(detOper, )
supermod.TSaudeCol.subclass = TSaudeColSub
# end class TSaudeColSub


class TRemunOutrasEmpresasSub(supermod.TRemunOutrasEmpresas):
    def __init__(self, tpInsc=None, nrInsc=None, codCateg=None, vlrRemunOE=None):
        super(TRemunOutrasEmpresasSub, self).__init__(tpInsc, nrInsc, codCateg, vlrRemunOE, )
supermod.TRemunOutrasEmpresas.subclass = TRemunOutrasEmpresasSub
# end class TRemunOutrasEmpresasSub


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


class evtDesligTypeSub(supermod.evtDesligType):
    def __init__(self, Id=None, ideEvento=None, ideEmpregador=None, ideVinculo=None, infoDeslig=None):
        super(evtDesligTypeSub, self).__init__(Id, ideEvento, ideEmpregador, ideVinculo, infoDeslig, )
supermod.evtDesligType.subclass = evtDesligTypeSub
# end class evtDesligTypeSub


class infoDesligTypeSub(supermod.infoDesligType):
    def __init__(self, mtvDeslig=None, dtDeslig=None, indPagtoAPI=None, dtProjFimAPI=None, pensAlim=None, percAliment=None, vrAlim=None, nrCertObito=None, nrProcTrab=None, indCumprParc=None, qtdDiasInterm=None, observacoes=None, sucessaoVinc=None, transfTit=None, verbasResc=None, quarentena=None, consigFGTS=None):
        super(infoDesligTypeSub, self).__init__(mtvDeslig, dtDeslig, indPagtoAPI, dtProjFimAPI, pensAlim, percAliment, vrAlim, nrCertObito, nrProcTrab, indCumprParc, qtdDiasInterm, observacoes, sucessaoVinc, transfTit, verbasResc, quarentena, consigFGTS, )
supermod.infoDesligType.subclass = infoDesligTypeSub
# end class infoDesligTypeSub


class observacoesTypeSub(supermod.observacoesType):
    def __init__(self, observacao=None):
        super(observacoesTypeSub, self).__init__(observacao, )
supermod.observacoesType.subclass = observacoesTypeSub
# end class observacoesTypeSub


class sucessaoVincTypeSub(supermod.sucessaoVincType):
    def __init__(self, cnpjSucessora=None):
        super(sucessaoVincTypeSub, self).__init__(cnpjSucessora, )
supermod.sucessaoVincType.subclass = sucessaoVincTypeSub
# end class sucessaoVincTypeSub


class transfTitTypeSub(supermod.transfTitType):
    def __init__(self, cpfSubstituto=None, dtNascto=None):
        super(transfTitTypeSub, self).__init__(cpfSubstituto, dtNascto, )
supermod.transfTitType.subclass = transfTitTypeSub
# end class transfTitTypeSub


class verbasRescTypeSub(supermod.verbasRescType):
    def __init__(self, dmDev=None, procJudTrab=None, infoMV=None, procCS=None):
        super(verbasRescTypeSub, self).__init__(dmDev, procJudTrab, infoMV, procCS, )
supermod.verbasRescType.subclass = verbasRescTypeSub
# end class verbasRescTypeSub


class dmDevTypeSub(supermod.dmDevType):
    def __init__(self, ideDmDev=None, infoPerApur=None, infoPerAnt=None, infoTrabInterm=None):
        super(dmDevTypeSub, self).__init__(ideDmDev, infoPerApur, infoPerAnt, infoTrabInterm, )
supermod.dmDevType.subclass = dmDevTypeSub
# end class dmDevTypeSub


class infoPerApurTypeSub(supermod.infoPerApurType):
    def __init__(self, ideEstabLot=None):
        super(infoPerApurTypeSub, self).__init__(ideEstabLot, )
supermod.infoPerApurType.subclass = infoPerApurTypeSub
# end class infoPerApurTypeSub


class ideEstabLotTypeSub(supermod.ideEstabLotType):
    def __init__(self, tpInsc=None, nrInsc=None, codLotacao=None, detVerbas=None, infoSaudeColet=None, infoAgNocivo=None, infoSimples=None):
        super(ideEstabLotTypeSub, self).__init__(tpInsc, nrInsc, codLotacao, detVerbas, infoSaudeColet, infoAgNocivo, infoSimples, )
supermod.ideEstabLotType.subclass = ideEstabLotTypeSub
# end class ideEstabLotTypeSub


class detVerbasTypeSub(supermod.detVerbasType):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None):
        super(detVerbasTypeSub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, )
supermod.detVerbasType.subclass = detVerbasTypeSub
# end class detVerbasTypeSub


class infoAgNocivoTypeSub(supermod.infoAgNocivoType):
    def __init__(self, grauExp=None):
        super(infoAgNocivoTypeSub, self).__init__(grauExp, )
supermod.infoAgNocivoType.subclass = infoAgNocivoTypeSub
# end class infoAgNocivoTypeSub


class infoSimplesTypeSub(supermod.infoSimplesType):
    def __init__(self, indSimples=None):
        super(infoSimplesTypeSub, self).__init__(indSimples, )
supermod.infoSimplesType.subclass = infoSimplesTypeSub
# end class infoSimplesTypeSub


class infoPerAntTypeSub(supermod.infoPerAntType):
    def __init__(self, ideADC=None):
        super(infoPerAntTypeSub, self).__init__(ideADC, )
supermod.infoPerAntType.subclass = infoPerAntTypeSub
# end class infoPerAntTypeSub


class ideADCTypeSub(supermod.ideADCType):
    def __init__(self, dtAcConv=None, tpAcConv=None, compAcConv=None, dtEfAcConv=None, dsc=None, idePeriodo=None):
        super(ideADCTypeSub, self).__init__(dtAcConv, tpAcConv, compAcConv, dtEfAcConv, dsc, idePeriodo, )
supermod.ideADCType.subclass = ideADCTypeSub
# end class ideADCTypeSub


class idePeriodoTypeSub(supermod.idePeriodoType):
    def __init__(self, perRef=None, ideEstabLot=None):
        super(idePeriodoTypeSub, self).__init__(perRef, ideEstabLot, )
supermod.idePeriodoType.subclass = idePeriodoTypeSub
# end class idePeriodoTypeSub


class ideEstabLotType1Sub(supermod.ideEstabLotType1):
    def __init__(self, tpInsc=None, nrInsc=None, codLotacao=None, detVerbas=None, infoAgNocivo=None, infoSimples=None):
        super(ideEstabLotType1Sub, self).__init__(tpInsc, nrInsc, codLotacao, detVerbas, infoAgNocivo, infoSimples, )
supermod.ideEstabLotType1.subclass = ideEstabLotType1Sub
# end class ideEstabLotType1Sub


class detVerbasType5Sub(supermod.detVerbasType5):
    def __init__(self, codRubr=None, ideTabRubr=None, qtdRubr=None, fatorRubr=None, vrUnit=None, vrRubr=None):
        super(detVerbasType5Sub, self).__init__(codRubr, ideTabRubr, qtdRubr, fatorRubr, vrUnit, vrRubr, )
supermod.detVerbasType5.subclass = detVerbasType5Sub
# end class detVerbasType5Sub


class infoAgNocivoType12Sub(supermod.infoAgNocivoType12):
    def __init__(self, grauExp=None):
        super(infoAgNocivoType12Sub, self).__init__(grauExp, )
supermod.infoAgNocivoType12.subclass = infoAgNocivoType12Sub
# end class infoAgNocivoType12Sub


class infoSimplesType14Sub(supermod.infoSimplesType14):
    def __init__(self, indSimples=None):
        super(infoSimplesType14Sub, self).__init__(indSimples, )
supermod.infoSimplesType14.subclass = infoSimplesType14Sub
# end class infoSimplesType14Sub


class infoTrabIntermTypeSub(supermod.infoTrabIntermType):
    def __init__(self, codConv=None):
        super(infoTrabIntermTypeSub, self).__init__(codConv, )
supermod.infoTrabIntermType.subclass = infoTrabIntermTypeSub
# end class infoTrabIntermTypeSub


class procJudTrabTypeSub(supermod.procJudTrabType):
    def __init__(self, tpTrib=None, nrProcJud=None, codSusp=None):
        super(procJudTrabTypeSub, self).__init__(tpTrib, nrProcJud, codSusp, )
supermod.procJudTrabType.subclass = procJudTrabTypeSub
# end class procJudTrabTypeSub


class infoMVTypeSub(supermod.infoMVType):
    def __init__(self, indMV=None, remunOutrEmpr=None):
        super(infoMVTypeSub, self).__init__(indMV, remunOutrEmpr, )
supermod.infoMVType.subclass = infoMVTypeSub
# end class infoMVTypeSub


class procCSTypeSub(supermod.procCSType):
    def __init__(self, nrProcJud=None):
        super(procCSTypeSub, self).__init__(nrProcJud, )
supermod.procCSType.subclass = procCSTypeSub
# end class procCSTypeSub


class quarentenaTypeSub(supermod.quarentenaType):
    def __init__(self, dtFimQuar=None):
        super(quarentenaTypeSub, self).__init__(dtFimQuar, )
supermod.quarentenaType.subclass = quarentenaTypeSub
# end class quarentenaTypeSub


class consigFGTSTypeSub(supermod.consigFGTSType):
    def __init__(self, insConsig=None, nrContr=None):
        super(consigFGTSTypeSub, self).__init__(insConsig, nrContr, )
supermod.consigFGTSType.subclass = consigFGTSTypeSub
# end class consigFGTSTypeSub


class detOperTypeSub(supermod.detOperType):
    def __init__(self, cnpjOper=None, regANS=None, vrPgTit=None, detPlano=None):
        super(detOperTypeSub, self).__init__(cnpjOper, regANS, vrPgTit, detPlano, )
supermod.detOperType.subclass = detOperTypeSub
# end class detOperTypeSub


class detPlanoTypeSub(supermod.detPlanoType):
    def __init__(self, tpDep=None, cpfDep=None, nmDep=None, dtNascto=None, vlrPgDep=None):
        super(detPlanoTypeSub, self).__init__(tpDep, cpfDep, nmDep, dtNascto, vlrPgDep, )
supermod.detPlanoType.subclass = detPlanoTypeSub
# end class detPlanoTypeSub


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
        sys.stdout.write('#from evtDeslig import *\n\n')
        sys.stdout.write('import evtDeslig as model_\n\n')
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
