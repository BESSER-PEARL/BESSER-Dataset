





import java.util.List;
import java.util.ArrayList;

public class xhtml_Inline  {

    private String mixed;
    private String inline;





    private List<xhtml_CodeType> xhtml_codetypes;




    private List<xhtml_BdoType> xhtml_bdotypes;




    private List<xhtml_BrType> xhtml_brtypes;




    private List<xhtml_SampType> xhtml_samptypes;




    private List<xhtml_AType> xhtml_atypes;




    private List<xhtml_DfnType> xhtml_dfntypes;




    private List<xhtml_KbdType> xhtml_kbdtypes;




    private List<xhtml_QType> xhtml_qtypes;




    private List<xhtml_SpanType> xhtml_spantypes;




    private List<xhtml_SmallType> xhtml_smalltypes;




    private List<xhtml_SubType> xhtml_subtypes;




    private List<xhtml_StrongType> xhtml_strongtypes;




    private List<xhtml_SupType> xhtml_suptypes;




    private List<xhtml_BType> xhtml_btypes;




    private List<xhtml_CiteType> xhtml_citetypes;




    private List<xhtml_ImgType> xhtml_imgtypes;




    private List<xhtml_MapType> xhtml_maptypes;




    private List<xhtml_AbbrType> xhtml_abbrtypes;




    private List<xhtml_EmType> xhtml_emtypes;




    private List<xhtml_BigType> xhtml_bigtypes;




    private List<xhtml_TtType> xhtml_tttypes;




    private List<xhtml_AcronymType> xhtml_acronymtypes;




    private List<xhtml_IType> xhtml_itypes;




    private List<xhtml_VarType> xhtml_vartypes;


    public xhtml_Inline(
        String mixed,        String inline    ) {
        this.mixed = mixed;
        this.inline = inline;
        this.xhtml_codetypes = new ArrayList<>();
        this.xhtml_bdotypes = new ArrayList<>();
        this.xhtml_brtypes = new ArrayList<>();
        this.xhtml_samptypes = new ArrayList<>();
        this.xhtml_atypes = new ArrayList<>();
        this.xhtml_dfntypes = new ArrayList<>();
        this.xhtml_kbdtypes = new ArrayList<>();
        this.xhtml_qtypes = new ArrayList<>();
        this.xhtml_spantypes = new ArrayList<>();
        this.xhtml_smalltypes = new ArrayList<>();
        this.xhtml_subtypes = new ArrayList<>();
        this.xhtml_strongtypes = new ArrayList<>();
        this.xhtml_suptypes = new ArrayList<>();
        this.xhtml_btypes = new ArrayList<>();
        this.xhtml_citetypes = new ArrayList<>();
        this.xhtml_imgtypes = new ArrayList<>();
        this.xhtml_maptypes = new ArrayList<>();
        this.xhtml_abbrtypes = new ArrayList<>();
        this.xhtml_emtypes = new ArrayList<>();
        this.xhtml_bigtypes = new ArrayList<>();
        this.xhtml_tttypes = new ArrayList<>();
        this.xhtml_acronymtypes = new ArrayList<>();
        this.xhtml_itypes = new ArrayList<>();
        this.xhtml_vartypes = new ArrayList<>();
    }

    public xhtml_Inline(
        String mixed,        String inline        ArrayList<xhtml_CodeType> xhtml_codetypes,        ArrayList<xhtml_BdoType> xhtml_bdotypes,        ArrayList<xhtml_BrType> xhtml_brtypes,        ArrayList<xhtml_SampType> xhtml_samptypes,        ArrayList<xhtml_AType> xhtml_atypes,        ArrayList<xhtml_DfnType> xhtml_dfntypes,        ArrayList<xhtml_KbdType> xhtml_kbdtypes,        ArrayList<xhtml_QType> xhtml_qtypes,        ArrayList<xhtml_SpanType> xhtml_spantypes,        ArrayList<xhtml_SmallType> xhtml_smalltypes,        ArrayList<xhtml_SubType> xhtml_subtypes,        ArrayList<xhtml_StrongType> xhtml_strongtypes,        ArrayList<xhtml_SupType> xhtml_suptypes,        ArrayList<xhtml_BType> xhtml_btypes,        ArrayList<xhtml_CiteType> xhtml_citetypes,        ArrayList<xhtml_ImgType> xhtml_imgtypes,        ArrayList<xhtml_MapType> xhtml_maptypes,        ArrayList<xhtml_AbbrType> xhtml_abbrtypes,        ArrayList<xhtml_EmType> xhtml_emtypes,        ArrayList<xhtml_BigType> xhtml_bigtypes,        ArrayList<xhtml_TtType> xhtml_tttypes,        ArrayList<xhtml_AcronymType> xhtml_acronymtypes,        ArrayList<xhtml_IType> xhtml_itypes,        ArrayList<xhtml_VarType> xhtml_vartypes    ) {
        this.mixed = mixed;
        this.inline = inline;
        this.xhtml_codetypes = xhtml_codetypes;
        this.xhtml_bdotypes = xhtml_bdotypes;
        this.xhtml_brtypes = xhtml_brtypes;
        this.xhtml_samptypes = xhtml_samptypes;
        this.xhtml_atypes = xhtml_atypes;
        this.xhtml_dfntypes = xhtml_dfntypes;
        this.xhtml_kbdtypes = xhtml_kbdtypes;
        this.xhtml_qtypes = xhtml_qtypes;
        this.xhtml_spantypes = xhtml_spantypes;
        this.xhtml_smalltypes = xhtml_smalltypes;
        this.xhtml_subtypes = xhtml_subtypes;
        this.xhtml_strongtypes = xhtml_strongtypes;
        this.xhtml_suptypes = xhtml_suptypes;
        this.xhtml_btypes = xhtml_btypes;
        this.xhtml_citetypes = xhtml_citetypes;
        this.xhtml_imgtypes = xhtml_imgtypes;
        this.xhtml_maptypes = xhtml_maptypes;
        this.xhtml_abbrtypes = xhtml_abbrtypes;
        this.xhtml_emtypes = xhtml_emtypes;
        this.xhtml_bigtypes = xhtml_bigtypes;
        this.xhtml_tttypes = xhtml_tttypes;
        this.xhtml_acronymtypes = xhtml_acronymtypes;
        this.xhtml_itypes = xhtml_itypes;
        this.xhtml_vartypes = xhtml_vartypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getInline() {
        return inline;
    }

    public void setInline(String inline) {
        this.inline = inline;
    }

    public List<xhtml_CodeType> getXhtml_codetypes() {
        return xhtml_codetypes;
    }

    public void addXhtml_codetype(Xhtml_codetype xhtml_codetype) {
        this.xhtml_codetypes.add(xhtml_codetype);
    }
    public List<xhtml_BdoType> getXhtml_bdotypes() {
        return xhtml_bdotypes;
    }

    public void addXhtml_bdotype(Xhtml_bdotype xhtml_bdotype) {
        this.xhtml_bdotypes.add(xhtml_bdotype);
    }
    public List<xhtml_BrType> getXhtml_brtypes() {
        return xhtml_brtypes;
    }

    public void addXhtml_brtype(Xhtml_brtype xhtml_brtype) {
        this.xhtml_brtypes.add(xhtml_brtype);
    }
    public List<xhtml_SampType> getXhtml_samptypes() {
        return xhtml_samptypes;
    }

    public void addXhtml_samptype(Xhtml_samptype xhtml_samptype) {
        this.xhtml_samptypes.add(xhtml_samptype);
    }
    public List<xhtml_AType> getXhtml_atypes() {
        return xhtml_atypes;
    }

    public void addXhtml_atype(Xhtml_atype xhtml_atype) {
        this.xhtml_atypes.add(xhtml_atype);
    }
    public List<xhtml_DfnType> getXhtml_dfntypes() {
        return xhtml_dfntypes;
    }

    public void addXhtml_dfntype(Xhtml_dfntype xhtml_dfntype) {
        this.xhtml_dfntypes.add(xhtml_dfntype);
    }
    public List<xhtml_KbdType> getXhtml_kbdtypes() {
        return xhtml_kbdtypes;
    }

    public void addXhtml_kbdtype(Xhtml_kbdtype xhtml_kbdtype) {
        this.xhtml_kbdtypes.add(xhtml_kbdtype);
    }
    public List<xhtml_QType> getXhtml_qtypes() {
        return xhtml_qtypes;
    }

    public void addXhtml_qtype(Xhtml_qtype xhtml_qtype) {
        this.xhtml_qtypes.add(xhtml_qtype);
    }
    public List<xhtml_SpanType> getXhtml_spantypes() {
        return xhtml_spantypes;
    }

    public void addXhtml_spantype(Xhtml_spantype xhtml_spantype) {
        this.xhtml_spantypes.add(xhtml_spantype);
    }
    public List<xhtml_SmallType> getXhtml_smalltypes() {
        return xhtml_smalltypes;
    }

    public void addXhtml_smalltype(Xhtml_smalltype xhtml_smalltype) {
        this.xhtml_smalltypes.add(xhtml_smalltype);
    }
    public List<xhtml_SubType> getXhtml_subtypes() {
        return xhtml_subtypes;
    }

    public void addXhtml_subtype(Xhtml_subtype xhtml_subtype) {
        this.xhtml_subtypes.add(xhtml_subtype);
    }
    public List<xhtml_StrongType> getXhtml_strongtypes() {
        return xhtml_strongtypes;
    }

    public void addXhtml_strongtype(Xhtml_strongtype xhtml_strongtype) {
        this.xhtml_strongtypes.add(xhtml_strongtype);
    }
    public List<xhtml_SupType> getXhtml_suptypes() {
        return xhtml_suptypes;
    }

    public void addXhtml_suptype(Xhtml_suptype xhtml_suptype) {
        this.xhtml_suptypes.add(xhtml_suptype);
    }
    public List<xhtml_BType> getXhtml_btypes() {
        return xhtml_btypes;
    }

    public void addXhtml_btype(Xhtml_btype xhtml_btype) {
        this.xhtml_btypes.add(xhtml_btype);
    }
    public List<xhtml_CiteType> getXhtml_citetypes() {
        return xhtml_citetypes;
    }

    public void addXhtml_citetype(Xhtml_citetype xhtml_citetype) {
        this.xhtml_citetypes.add(xhtml_citetype);
    }
    public List<xhtml_ImgType> getXhtml_imgtypes() {
        return xhtml_imgtypes;
    }

    public void addXhtml_imgtype(Xhtml_imgtype xhtml_imgtype) {
        this.xhtml_imgtypes.add(xhtml_imgtype);
    }
    public List<xhtml_MapType> getXhtml_maptypes() {
        return xhtml_maptypes;
    }

    public void addXhtml_maptype(Xhtml_maptype xhtml_maptype) {
        this.xhtml_maptypes.add(xhtml_maptype);
    }
    public List<xhtml_AbbrType> getXhtml_abbrtypes() {
        return xhtml_abbrtypes;
    }

    public void addXhtml_abbrtype(Xhtml_abbrtype xhtml_abbrtype) {
        this.xhtml_abbrtypes.add(xhtml_abbrtype);
    }
    public List<xhtml_EmType> getXhtml_emtypes() {
        return xhtml_emtypes;
    }

    public void addXhtml_emtype(Xhtml_emtype xhtml_emtype) {
        this.xhtml_emtypes.add(xhtml_emtype);
    }
    public List<xhtml_BigType> getXhtml_bigtypes() {
        return xhtml_bigtypes;
    }

    public void addXhtml_bigtype(Xhtml_bigtype xhtml_bigtype) {
        this.xhtml_bigtypes.add(xhtml_bigtype);
    }
    public List<xhtml_TtType> getXhtml_tttypes() {
        return xhtml_tttypes;
    }

    public void addXhtml_tttype(Xhtml_tttype xhtml_tttype) {
        this.xhtml_tttypes.add(xhtml_tttype);
    }
    public List<xhtml_AcronymType> getXhtml_acronymtypes() {
        return xhtml_acronymtypes;
    }

    public void addXhtml_acronymtype(Xhtml_acronymtype xhtml_acronymtype) {
        this.xhtml_acronymtypes.add(xhtml_acronymtype);
    }
    public List<xhtml_IType> getXhtml_itypes() {
        return xhtml_itypes;
    }

    public void addXhtml_itype(Xhtml_itype xhtml_itype) {
        this.xhtml_itypes.add(xhtml_itype);
    }
    public List<xhtml_VarType> getXhtml_vartypes() {
        return xhtml_vartypes;
    }

    public void addXhtml_vartype(Xhtml_vartype xhtml_vartype) {
        this.xhtml_vartypes.add(xhtml_vartype);
    }

}