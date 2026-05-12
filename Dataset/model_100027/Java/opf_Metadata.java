





import java.util.List;
import java.util.ArrayList;

public class opf_Metadata  {






    private List<opf_Date> opf_dates;




    private List<opf_Identifier> opf_identifiers;




    private List<opf_Coverage> opf_coverages;




    private List<opf_Language> opf_languages;




    private List<opf_Rights> opf_rightss;




    private List<opf_Source> opf_sources;




    private List<opf_Type> opf_types;




    private List<opf_Relation> opf_relations;




    private List<opf_Meta> opf_metas;




    private List<opf_Contributor> opf_contributors;


    public opf_Metadata(
    ) {
        this.opf_dates = new ArrayList<>();
        this.opf_identifiers = new ArrayList<>();
        this.opf_coverages = new ArrayList<>();
        this.opf_languages = new ArrayList<>();
        this.opf_rightss = new ArrayList<>();
        this.opf_sources = new ArrayList<>();
        this.opf_types = new ArrayList<>();
        this.opf_relations = new ArrayList<>();
        this.opf_metas = new ArrayList<>();
        this.opf_contributors = new ArrayList<>();
    }

    public opf_Metadata(
        ArrayList<opf_Date> opf_dates,        ArrayList<opf_Identifier> opf_identifiers,        ArrayList<opf_Coverage> opf_coverages,        ArrayList<opf_Language> opf_languages,        ArrayList<opf_Rights> opf_rightss,        ArrayList<opf_Source> opf_sources,        ArrayList<opf_Type> opf_types,        ArrayList<opf_Relation> opf_relations,        ArrayList<opf_Meta> opf_metas,        ArrayList<opf_Contributor> opf_contributors    ) {
        this.opf_dates = opf_dates;
        this.opf_identifiers = opf_identifiers;
        this.opf_coverages = opf_coverages;
        this.opf_languages = opf_languages;
        this.opf_rightss = opf_rightss;
        this.opf_sources = opf_sources;
        this.opf_types = opf_types;
        this.opf_relations = opf_relations;
        this.opf_metas = opf_metas;
        this.opf_contributors = opf_contributors;
    }


    public List<opf_Date> getOpf_dates() {
        return opf_dates;
    }

    public void addOpf_date(Opf_date opf_date) {
        this.opf_dates.add(opf_date);
    }
    public List<opf_Identifier> getOpf_identifiers() {
        return opf_identifiers;
    }

    public void addOpf_identifier(Opf_identifier opf_identifier) {
        this.opf_identifiers.add(opf_identifier);
    }
    public List<opf_Coverage> getOpf_coverages() {
        return opf_coverages;
    }

    public void addOpf_coverage(Opf_coverage opf_coverage) {
        this.opf_coverages.add(opf_coverage);
    }
    public List<opf_Language> getOpf_languages() {
        return opf_languages;
    }

    public void addOpf_language(Opf_language opf_language) {
        this.opf_languages.add(opf_language);
    }
    public List<opf_Rights> getOpf_rightss() {
        return opf_rightss;
    }

    public void addOpf_rights(Opf_rights opf_rights) {
        this.opf_rightss.add(opf_rights);
    }
    public List<opf_Source> getOpf_sources() {
        return opf_sources;
    }

    public void addOpf_source(Opf_source opf_source) {
        this.opf_sources.add(opf_source);
    }
    public List<opf_Type> getOpf_types() {
        return opf_types;
    }

    public void addOpf_type(Opf_type opf_type) {
        this.opf_types.add(opf_type);
    }
    public List<opf_Relation> getOpf_relations() {
        return opf_relations;
    }

    public void addOpf_relation(Opf_relation opf_relation) {
        this.opf_relations.add(opf_relation);
    }
    public List<opf_Meta> getOpf_metas() {
        return opf_metas;
    }

    public void addOpf_meta(Opf_meta opf_meta) {
        this.opf_metas.add(opf_meta);
    }
    public List<opf_Contributor> getOpf_contributors() {
        return opf_contributors;
    }

    public void addOpf_contributor(Opf_contributor opf_contributor) {
        this.opf_contributors.add(opf_contributor);
    }

}