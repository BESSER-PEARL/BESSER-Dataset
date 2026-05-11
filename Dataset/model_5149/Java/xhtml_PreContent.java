





import java.util.List;
import java.util.ArrayList;

public class xhtml_PreContent  {

    private String group;
    private String mixed;





    private List<xhtml_Tt> xhtml_tts;




    private List<xhtml_Strong> xhtml_strongs;




    private List<xhtml_Cite> xhtml_cites;




    private List<xhtml_Br> xhtml_brs;




    private List<xhtml_Q> xhtml_qs;




    private List<xhtml_Span> xhtml_spans;




    private List<xhtml_I> xhtml_is;




    private List<xhtml_Acronym> xhtml_acronyms;




    private List<xhtml_A> xhtml_as;




    private List<xhtml_Big> xhtml_bigs;




    private List<xhtml_Small> xhtml_smalls;




    private List<xhtml_Kbd> xhtml_kbds;




    private List<xhtml_Code> xhtml_codes;




    private List<xhtml_B> xhtml_bs;




    private List<xhtml_Sup> xhtml_sups;




    private List<xhtml_Var> xhtml_vars;




    private List<xhtml_Em> xhtml_ems;




    private List<xhtml_Sub> xhtml_subs;




    private List<xhtml_Dfn> xhtml_dfns;




    private List<xhtml_Samp> xhtml_samps;




    private List<xhtml_Abbr> xhtml_abbrs;


    public xhtml_PreContent(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
        this.xhtml_tts = new ArrayList<>();
        this.xhtml_strongs = new ArrayList<>();
        this.xhtml_cites = new ArrayList<>();
        this.xhtml_brs = new ArrayList<>();
        this.xhtml_qs = new ArrayList<>();
        this.xhtml_spans = new ArrayList<>();
        this.xhtml_is = new ArrayList<>();
        this.xhtml_acronyms = new ArrayList<>();
        this.xhtml_as = new ArrayList<>();
        this.xhtml_bigs = new ArrayList<>();
        this.xhtml_smalls = new ArrayList<>();
        this.xhtml_kbds = new ArrayList<>();
        this.xhtml_codes = new ArrayList<>();
        this.xhtml_bs = new ArrayList<>();
        this.xhtml_sups = new ArrayList<>();
        this.xhtml_vars = new ArrayList<>();
        this.xhtml_ems = new ArrayList<>();
        this.xhtml_subs = new ArrayList<>();
        this.xhtml_dfns = new ArrayList<>();
        this.xhtml_samps = new ArrayList<>();
        this.xhtml_abbrs = new ArrayList<>();
    }

    public xhtml_PreContent(
        String group,        String mixed        ArrayList<xhtml_Tt> xhtml_tts,        ArrayList<xhtml_Strong> xhtml_strongs,        ArrayList<xhtml_Cite> xhtml_cites,        ArrayList<xhtml_Br> xhtml_brs,        ArrayList<xhtml_Q> xhtml_qs,        ArrayList<xhtml_Span> xhtml_spans,        ArrayList<xhtml_I> xhtml_is,        ArrayList<xhtml_Acronym> xhtml_acronyms,        ArrayList<xhtml_A> xhtml_as,        ArrayList<xhtml_Big> xhtml_bigs,        ArrayList<xhtml_Small> xhtml_smalls,        ArrayList<xhtml_Kbd> xhtml_kbds,        ArrayList<xhtml_Code> xhtml_codes,        ArrayList<xhtml_B> xhtml_bs,        ArrayList<xhtml_Sup> xhtml_sups,        ArrayList<xhtml_Var> xhtml_vars,        ArrayList<xhtml_Em> xhtml_ems,        ArrayList<xhtml_Sub> xhtml_subs,        ArrayList<xhtml_Dfn> xhtml_dfns,        ArrayList<xhtml_Samp> xhtml_samps,        ArrayList<xhtml_Abbr> xhtml_abbrs    ) {
        this.group = group;
        this.mixed = mixed;
        this.xhtml_tts = xhtml_tts;
        this.xhtml_strongs = xhtml_strongs;
        this.xhtml_cites = xhtml_cites;
        this.xhtml_brs = xhtml_brs;
        this.xhtml_qs = xhtml_qs;
        this.xhtml_spans = xhtml_spans;
        this.xhtml_is = xhtml_is;
        this.xhtml_acronyms = xhtml_acronyms;
        this.xhtml_as = xhtml_as;
        this.xhtml_bigs = xhtml_bigs;
        this.xhtml_smalls = xhtml_smalls;
        this.xhtml_kbds = xhtml_kbds;
        this.xhtml_codes = xhtml_codes;
        this.xhtml_bs = xhtml_bs;
        this.xhtml_sups = xhtml_sups;
        this.xhtml_vars = xhtml_vars;
        this.xhtml_ems = xhtml_ems;
        this.xhtml_subs = xhtml_subs;
        this.xhtml_dfns = xhtml_dfns;
        this.xhtml_samps = xhtml_samps;
        this.xhtml_abbrs = xhtml_abbrs;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<xhtml_Tt> getXhtml_tts() {
        return xhtml_tts;
    }

    public void addXhtml_tt(Xhtml_tt xhtml_tt) {
        this.xhtml_tts.add(xhtml_tt);
    }
    public List<xhtml_Strong> getXhtml_strongs() {
        return xhtml_strongs;
    }

    public void addXhtml_strong(Xhtml_strong xhtml_strong) {
        this.xhtml_strongs.add(xhtml_strong);
    }
    public List<xhtml_Cite> getXhtml_cites() {
        return xhtml_cites;
    }

    public void addXhtml_cite(Xhtml_cite xhtml_cite) {
        this.xhtml_cites.add(xhtml_cite);
    }
    public List<xhtml_Br> getXhtml_brs() {
        return xhtml_brs;
    }

    public void addXhtml_br(Xhtml_br xhtml_br) {
        this.xhtml_brs.add(xhtml_br);
    }
    public List<xhtml_Q> getXhtml_qs() {
        return xhtml_qs;
    }

    public void addXhtml_q(Xhtml_q xhtml_q) {
        this.xhtml_qs.add(xhtml_q);
    }
    public List<xhtml_Span> getXhtml_spans() {
        return xhtml_spans;
    }

    public void addXhtml_span(Xhtml_span xhtml_span) {
        this.xhtml_spans.add(xhtml_span);
    }
    public List<xhtml_I> getXhtml_is() {
        return xhtml_is;
    }

    public void addXhtml_i(Xhtml_i xhtml_i) {
        this.xhtml_is.add(xhtml_i);
    }
    public List<xhtml_Acronym> getXhtml_acronyms() {
        return xhtml_acronyms;
    }

    public void addXhtml_acronym(Xhtml_acronym xhtml_acronym) {
        this.xhtml_acronyms.add(xhtml_acronym);
    }
    public List<xhtml_A> getXhtml_as() {
        return xhtml_as;
    }

    public void addXhtml_a(Xhtml_a xhtml_a) {
        this.xhtml_as.add(xhtml_a);
    }
    public List<xhtml_Big> getXhtml_bigs() {
        return xhtml_bigs;
    }

    public void addXhtml_big(Xhtml_big xhtml_big) {
        this.xhtml_bigs.add(xhtml_big);
    }
    public List<xhtml_Small> getXhtml_smalls() {
        return xhtml_smalls;
    }

    public void addXhtml_small(Xhtml_small xhtml_small) {
        this.xhtml_smalls.add(xhtml_small);
    }
    public List<xhtml_Kbd> getXhtml_kbds() {
        return xhtml_kbds;
    }

    public void addXhtml_kbd(Xhtml_kbd xhtml_kbd) {
        this.xhtml_kbds.add(xhtml_kbd);
    }
    public List<xhtml_Code> getXhtml_codes() {
        return xhtml_codes;
    }

    public void addXhtml_code(Xhtml_code xhtml_code) {
        this.xhtml_codes.add(xhtml_code);
    }
    public List<xhtml_B> getXhtml_bs() {
        return xhtml_bs;
    }

    public void addXhtml_b(Xhtml_b xhtml_b) {
        this.xhtml_bs.add(xhtml_b);
    }
    public List<xhtml_Sup> getXhtml_sups() {
        return xhtml_sups;
    }

    public void addXhtml_sup(Xhtml_sup xhtml_sup) {
        this.xhtml_sups.add(xhtml_sup);
    }
    public List<xhtml_Var> getXhtml_vars() {
        return xhtml_vars;
    }

    public void addXhtml_var(Xhtml_var xhtml_var) {
        this.xhtml_vars.add(xhtml_var);
    }
    public List<xhtml_Em> getXhtml_ems() {
        return xhtml_ems;
    }

    public void addXhtml_em(Xhtml_em xhtml_em) {
        this.xhtml_ems.add(xhtml_em);
    }
    public List<xhtml_Sub> getXhtml_subs() {
        return xhtml_subs;
    }

    public void addXhtml_sub(Xhtml_sub xhtml_sub) {
        this.xhtml_subs.add(xhtml_sub);
    }
    public List<xhtml_Dfn> getXhtml_dfns() {
        return xhtml_dfns;
    }

    public void addXhtml_dfn(Xhtml_dfn xhtml_dfn) {
        this.xhtml_dfns.add(xhtml_dfn);
    }
    public List<xhtml_Samp> getXhtml_samps() {
        return xhtml_samps;
    }

    public void addXhtml_samp(Xhtml_samp xhtml_samp) {
        this.xhtml_samps.add(xhtml_samp);
    }
    public List<xhtml_Abbr> getXhtml_abbrs() {
        return xhtml_abbrs;
    }

    public void addXhtml_abbr(Xhtml_abbr xhtml_abbr) {
        this.xhtml_abbrs.add(xhtml_abbr);
    }

}