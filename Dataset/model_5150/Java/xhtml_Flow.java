





import java.util.List;
import java.util.ArrayList;

public class xhtml_Flow  {

    private String mixed;
    private String group;





    private List<xhtml_Tt> xhtml_tts;




    private List<xhtml_Ul> xhtml_uls;




    private List<xhtml_Acronym> xhtml_acronyms;




    private List<xhtml_Table> xhtml_tables;




    private List<xhtml_Var> xhtml_vars;




    private List<xhtml_Pre> xhtml_pres;




    private List<xhtml_Span> xhtml_spans;




    private List<xhtml_Object> xhtml_objects;




    private List<xhtml_Code> xhtml_codes;




    private List<xhtml_B> xhtml_bs;




    private List<xhtml_P> xhtml_ps;




    private List<xhtml_Big> xhtml_bigs;




    private List<xhtml_Dl> xhtml_dls;




    private List<xhtml_Sup> xhtml_sups;




    private List<xhtml_Br> xhtml_brs;




    private List<xhtml_Div> xhtml_divs;




    private List<xhtml_Ol> xhtml_ols;




    private List<xhtml_Abbr> xhtml_abbrs;




    private List<xhtml_Q> xhtml_qs;




    private List<xhtml_Blockquote> xhtml_blockquotes;




    private List<xhtml_Small> xhtml_smalls;




    private List<xhtml_Em> xhtml_ems;




    private List<xhtml_Dfn> xhtml_dfns;




    private List<xhtml_Kbd> xhtml_kbds;




    private List<xhtml_Hr> xhtml_hrs;




    private List<xhtml_Samp> xhtml_samps;




    private List<xhtml_A> xhtml_as;




    private List<xhtml_I> xhtml_is;




    private List<xhtml_Sub> xhtml_subs;




    private List<xhtml_Cite> xhtml_cites;




    private List<xhtml_Img> xhtml_imgs;




    private List<xhtml_Strong> xhtml_strongs;


    public xhtml_Flow(
        String mixed,        String group    ) {
        this.mixed = mixed;
        this.group = group;
        this.xhtml_tts = new ArrayList<>();
        this.xhtml_uls = new ArrayList<>();
        this.xhtml_acronyms = new ArrayList<>();
        this.xhtml_tables = new ArrayList<>();
        this.xhtml_vars = new ArrayList<>();
        this.xhtml_pres = new ArrayList<>();
        this.xhtml_spans = new ArrayList<>();
        this.xhtml_objects = new ArrayList<>();
        this.xhtml_codes = new ArrayList<>();
        this.xhtml_bs = new ArrayList<>();
        this.xhtml_ps = new ArrayList<>();
        this.xhtml_bigs = new ArrayList<>();
        this.xhtml_dls = new ArrayList<>();
        this.xhtml_sups = new ArrayList<>();
        this.xhtml_brs = new ArrayList<>();
        this.xhtml_divs = new ArrayList<>();
        this.xhtml_ols = new ArrayList<>();
        this.xhtml_abbrs = new ArrayList<>();
        this.xhtml_qs = new ArrayList<>();
        this.xhtml_blockquotes = new ArrayList<>();
        this.xhtml_smalls = new ArrayList<>();
        this.xhtml_ems = new ArrayList<>();
        this.xhtml_dfns = new ArrayList<>();
        this.xhtml_kbds = new ArrayList<>();
        this.xhtml_hrs = new ArrayList<>();
        this.xhtml_samps = new ArrayList<>();
        this.xhtml_as = new ArrayList<>();
        this.xhtml_is = new ArrayList<>();
        this.xhtml_subs = new ArrayList<>();
        this.xhtml_cites = new ArrayList<>();
        this.xhtml_imgs = new ArrayList<>();
        this.xhtml_strongs = new ArrayList<>();
    }

    public xhtml_Flow(
        String mixed,        String group        ArrayList<xhtml_Tt> xhtml_tts,        ArrayList<xhtml_Ul> xhtml_uls,        ArrayList<xhtml_Acronym> xhtml_acronyms,        ArrayList<xhtml_Table> xhtml_tables,        ArrayList<xhtml_Var> xhtml_vars,        ArrayList<xhtml_Pre> xhtml_pres,        ArrayList<xhtml_Span> xhtml_spans,        ArrayList<xhtml_Object> xhtml_objects,        ArrayList<xhtml_Code> xhtml_codes,        ArrayList<xhtml_B> xhtml_bs,        ArrayList<xhtml_P> xhtml_ps,        ArrayList<xhtml_Big> xhtml_bigs,        ArrayList<xhtml_Dl> xhtml_dls,        ArrayList<xhtml_Sup> xhtml_sups,        ArrayList<xhtml_Br> xhtml_brs,        ArrayList<xhtml_Div> xhtml_divs,        ArrayList<xhtml_Ol> xhtml_ols,        ArrayList<xhtml_Abbr> xhtml_abbrs,        ArrayList<xhtml_Q> xhtml_qs,        ArrayList<xhtml_Blockquote> xhtml_blockquotes,        ArrayList<xhtml_Small> xhtml_smalls,        ArrayList<xhtml_Em> xhtml_ems,        ArrayList<xhtml_Dfn> xhtml_dfns,        ArrayList<xhtml_Kbd> xhtml_kbds,        ArrayList<xhtml_Hr> xhtml_hrs,        ArrayList<xhtml_Samp> xhtml_samps,        ArrayList<xhtml_A> xhtml_as,        ArrayList<xhtml_I> xhtml_is,        ArrayList<xhtml_Sub> xhtml_subs,        ArrayList<xhtml_Cite> xhtml_cites,        ArrayList<xhtml_Img> xhtml_imgs,        ArrayList<xhtml_Strong> xhtml_strongs    ) {
        this.mixed = mixed;
        this.group = group;
        this.xhtml_tts = xhtml_tts;
        this.xhtml_uls = xhtml_uls;
        this.xhtml_acronyms = xhtml_acronyms;
        this.xhtml_tables = xhtml_tables;
        this.xhtml_vars = xhtml_vars;
        this.xhtml_pres = xhtml_pres;
        this.xhtml_spans = xhtml_spans;
        this.xhtml_objects = xhtml_objects;
        this.xhtml_codes = xhtml_codes;
        this.xhtml_bs = xhtml_bs;
        this.xhtml_ps = xhtml_ps;
        this.xhtml_bigs = xhtml_bigs;
        this.xhtml_dls = xhtml_dls;
        this.xhtml_sups = xhtml_sups;
        this.xhtml_brs = xhtml_brs;
        this.xhtml_divs = xhtml_divs;
        this.xhtml_ols = xhtml_ols;
        this.xhtml_abbrs = xhtml_abbrs;
        this.xhtml_qs = xhtml_qs;
        this.xhtml_blockquotes = xhtml_blockquotes;
        this.xhtml_smalls = xhtml_smalls;
        this.xhtml_ems = xhtml_ems;
        this.xhtml_dfns = xhtml_dfns;
        this.xhtml_kbds = xhtml_kbds;
        this.xhtml_hrs = xhtml_hrs;
        this.xhtml_samps = xhtml_samps;
        this.xhtml_as = xhtml_as;
        this.xhtml_is = xhtml_is;
        this.xhtml_subs = xhtml_subs;
        this.xhtml_cites = xhtml_cites;
        this.xhtml_imgs = xhtml_imgs;
        this.xhtml_strongs = xhtml_strongs;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<xhtml_Tt> getXhtml_tts() {
        return xhtml_tts;
    }

    public void addXhtml_tt(Xhtml_tt xhtml_tt) {
        this.xhtml_tts.add(xhtml_tt);
    }
    public List<xhtml_Ul> getXhtml_uls() {
        return xhtml_uls;
    }

    public void addXhtml_ul(Xhtml_ul xhtml_ul) {
        this.xhtml_uls.add(xhtml_ul);
    }
    public List<xhtml_Acronym> getXhtml_acronyms() {
        return xhtml_acronyms;
    }

    public void addXhtml_acronym(Xhtml_acronym xhtml_acronym) {
        this.xhtml_acronyms.add(xhtml_acronym);
    }
    public List<xhtml_Table> getXhtml_tables() {
        return xhtml_tables;
    }

    public void addXhtml_table(Xhtml_table xhtml_table) {
        this.xhtml_tables.add(xhtml_table);
    }
    public List<xhtml_Var> getXhtml_vars() {
        return xhtml_vars;
    }

    public void addXhtml_var(Xhtml_var xhtml_var) {
        this.xhtml_vars.add(xhtml_var);
    }
    public List<xhtml_Pre> getXhtml_pres() {
        return xhtml_pres;
    }

    public void addXhtml_pre(Xhtml_pre xhtml_pre) {
        this.xhtml_pres.add(xhtml_pre);
    }
    public List<xhtml_Span> getXhtml_spans() {
        return xhtml_spans;
    }

    public void addXhtml_span(Xhtml_span xhtml_span) {
        this.xhtml_spans.add(xhtml_span);
    }
    public List<xhtml_Object> getXhtml_objects() {
        return xhtml_objects;
    }

    public void addXhtml_object(Xhtml_object xhtml_object) {
        this.xhtml_objects.add(xhtml_object);
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
    public List<xhtml_P> getXhtml_ps() {
        return xhtml_ps;
    }

    public void addXhtml_p(Xhtml_p xhtml_p) {
        this.xhtml_ps.add(xhtml_p);
    }
    public List<xhtml_Big> getXhtml_bigs() {
        return xhtml_bigs;
    }

    public void addXhtml_big(Xhtml_big xhtml_big) {
        this.xhtml_bigs.add(xhtml_big);
    }
    public List<xhtml_Dl> getXhtml_dls() {
        return xhtml_dls;
    }

    public void addXhtml_dl(Xhtml_dl xhtml_dl) {
        this.xhtml_dls.add(xhtml_dl);
    }
    public List<xhtml_Sup> getXhtml_sups() {
        return xhtml_sups;
    }

    public void addXhtml_sup(Xhtml_sup xhtml_sup) {
        this.xhtml_sups.add(xhtml_sup);
    }
    public List<xhtml_Br> getXhtml_brs() {
        return xhtml_brs;
    }

    public void addXhtml_br(Xhtml_br xhtml_br) {
        this.xhtml_brs.add(xhtml_br);
    }
    public List<xhtml_Div> getXhtml_divs() {
        return xhtml_divs;
    }

    public void addXhtml_div(Xhtml_div xhtml_div) {
        this.xhtml_divs.add(xhtml_div);
    }
    public List<xhtml_Ol> getXhtml_ols() {
        return xhtml_ols;
    }

    public void addXhtml_ol(Xhtml_ol xhtml_ol) {
        this.xhtml_ols.add(xhtml_ol);
    }
    public List<xhtml_Abbr> getXhtml_abbrs() {
        return xhtml_abbrs;
    }

    public void addXhtml_abbr(Xhtml_abbr xhtml_abbr) {
        this.xhtml_abbrs.add(xhtml_abbr);
    }
    public List<xhtml_Q> getXhtml_qs() {
        return xhtml_qs;
    }

    public void addXhtml_q(Xhtml_q xhtml_q) {
        this.xhtml_qs.add(xhtml_q);
    }
    public List<xhtml_Blockquote> getXhtml_blockquotes() {
        return xhtml_blockquotes;
    }

    public void addXhtml_blockquote(Xhtml_blockquote xhtml_blockquote) {
        this.xhtml_blockquotes.add(xhtml_blockquote);
    }
    public List<xhtml_Small> getXhtml_smalls() {
        return xhtml_smalls;
    }

    public void addXhtml_small(Xhtml_small xhtml_small) {
        this.xhtml_smalls.add(xhtml_small);
    }
    public List<xhtml_Em> getXhtml_ems() {
        return xhtml_ems;
    }

    public void addXhtml_em(Xhtml_em xhtml_em) {
        this.xhtml_ems.add(xhtml_em);
    }
    public List<xhtml_Dfn> getXhtml_dfns() {
        return xhtml_dfns;
    }

    public void addXhtml_dfn(Xhtml_dfn xhtml_dfn) {
        this.xhtml_dfns.add(xhtml_dfn);
    }
    public List<xhtml_Kbd> getXhtml_kbds() {
        return xhtml_kbds;
    }

    public void addXhtml_kbd(Xhtml_kbd xhtml_kbd) {
        this.xhtml_kbds.add(xhtml_kbd);
    }
    public List<xhtml_Hr> getXhtml_hrs() {
        return xhtml_hrs;
    }

    public void addXhtml_hr(Xhtml_hr xhtml_hr) {
        this.xhtml_hrs.add(xhtml_hr);
    }
    public List<xhtml_Samp> getXhtml_samps() {
        return xhtml_samps;
    }

    public void addXhtml_samp(Xhtml_samp xhtml_samp) {
        this.xhtml_samps.add(xhtml_samp);
    }
    public List<xhtml_A> getXhtml_as() {
        return xhtml_as;
    }

    public void addXhtml_a(Xhtml_a xhtml_a) {
        this.xhtml_as.add(xhtml_a);
    }
    public List<xhtml_I> getXhtml_is() {
        return xhtml_is;
    }

    public void addXhtml_i(Xhtml_i xhtml_i) {
        this.xhtml_is.add(xhtml_i);
    }
    public List<xhtml_Sub> getXhtml_subs() {
        return xhtml_subs;
    }

    public void addXhtml_sub(Xhtml_sub xhtml_sub) {
        this.xhtml_subs.add(xhtml_sub);
    }
    public List<xhtml_Cite> getXhtml_cites() {
        return xhtml_cites;
    }

    public void addXhtml_cite(Xhtml_cite xhtml_cite) {
        this.xhtml_cites.add(xhtml_cite);
    }
    public List<xhtml_Img> getXhtml_imgs() {
        return xhtml_imgs;
    }

    public void addXhtml_img(Xhtml_img xhtml_img) {
        this.xhtml_imgs.add(xhtml_img);
    }
    public List<xhtml_Strong> getXhtml_strongs() {
        return xhtml_strongs;
    }

    public void addXhtml_strong(Xhtml_strong xhtml_strong) {
        this.xhtml_strongs.add(xhtml_strong);
    }

}