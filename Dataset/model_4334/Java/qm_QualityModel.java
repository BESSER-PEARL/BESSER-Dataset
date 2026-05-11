





import java.util.List;
import java.util.ArrayList;

public class qm_QualityModel extends NamedElement {

    private String schoolGradeBoundary2;
    private String schoolGradeBoundary4;
    private String schoolGradeBoundary5;
    private String schoolGradeBoundary6;
    private String schoolGradeBoundary3;





    private List<qm_Evaluation> qm_evaluations;




    private List<qm_Tag> qm_tags;




    private qm_Evaluation qm_evaluation;




    private List<qm_QualityModel> qm_qualitymodels;




    private List<qm_MeasurementMethod> qm_measurementmethods;




    private List<qm_Source> qm_sources;




    private qm_Source qm_source;




    private qm_Entity qm_entity;




    private List<qm_Tool> qm_tools;




    private qm_MeasurementMethod qm_measurementmethod;




    private qm_Measure qm_measure;




    private List<qm_Factor> qm_factors;




    private List<qm_Measure> qm_measures;




    private qm_Tool qm_tool;




    private List<qm_Entity> qm_entitys;




    private qm_Tag qm_tag;




    private qm_Factor qm_factor;


    public qm_QualityModel(
        String schoolGradeBoundary2,        String schoolGradeBoundary4,        String schoolGradeBoundary5,        String schoolGradeBoundary6,        String schoolGradeBoundary3    ) {
        super(
        );
        this.schoolGradeBoundary2 = schoolGradeBoundary2;
        this.schoolGradeBoundary4 = schoolGradeBoundary4;
        this.schoolGradeBoundary5 = schoolGradeBoundary5;
        this.schoolGradeBoundary6 = schoolGradeBoundary6;
        this.schoolGradeBoundary3 = schoolGradeBoundary3;
        this.qm_evaluations = new ArrayList<>();
        this.qm_tags = new ArrayList<>();
        this.qm_qualitymodels = new ArrayList<>();
        this.qm_measurementmethods = new ArrayList<>();
        this.qm_sources = new ArrayList<>();
        this.qm_tools = new ArrayList<>();
        this.qm_factors = new ArrayList<>();
        this.qm_measures = new ArrayList<>();
        this.qm_entitys = new ArrayList<>();
    }

    public qm_QualityModel(
        String schoolGradeBoundary2,        String schoolGradeBoundary4,        String schoolGradeBoundary5,        String schoolGradeBoundary6,        String schoolGradeBoundary3        ArrayList<qm_Evaluation> qm_evaluations,        ArrayList<qm_Tag> qm_tags,        ArrayList<qm_QualityModel> qm_qualitymodels,        ArrayList<qm_MeasurementMethod> qm_measurementmethods,        ArrayList<qm_Source> qm_sources,        ArrayList<qm_Tool> qm_tools,        ArrayList<qm_Factor> qm_factors,        ArrayList<qm_Measure> qm_measures,        ArrayList<qm_Entity> qm_entitys    ) {
        this.schoolGradeBoundary2 = schoolGradeBoundary2;
        this.schoolGradeBoundary4 = schoolGradeBoundary4;
        this.schoolGradeBoundary5 = schoolGradeBoundary5;
        this.schoolGradeBoundary6 = schoolGradeBoundary6;
        this.schoolGradeBoundary3 = schoolGradeBoundary3;
        this.qm_evaluations = qm_evaluations;
        this.qm_tags = qm_tags;
        this.qm_qualitymodels = qm_qualitymodels;
        this.qm_measurementmethods = qm_measurementmethods;
        this.qm_sources = qm_sources;
        this.qm_tools = qm_tools;
        this.qm_factors = qm_factors;
        this.qm_measures = qm_measures;
        this.qm_entitys = qm_entitys;
    }

    public String getSchoolgradeboundary2() {
        return schoolGradeBoundary2;
    }

    public void setSchoolgradeboundary2(String schoolGradeBoundary2) {
        this.schoolGradeBoundary2 = schoolGradeBoundary2;
    }
    public String getSchoolgradeboundary4() {
        return schoolGradeBoundary4;
    }

    public void setSchoolgradeboundary4(String schoolGradeBoundary4) {
        this.schoolGradeBoundary4 = schoolGradeBoundary4;
    }
    public String getSchoolgradeboundary5() {
        return schoolGradeBoundary5;
    }

    public void setSchoolgradeboundary5(String schoolGradeBoundary5) {
        this.schoolGradeBoundary5 = schoolGradeBoundary5;
    }
    public String getSchoolgradeboundary6() {
        return schoolGradeBoundary6;
    }

    public void setSchoolgradeboundary6(String schoolGradeBoundary6) {
        this.schoolGradeBoundary6 = schoolGradeBoundary6;
    }
    public String getSchoolgradeboundary3() {
        return schoolGradeBoundary3;
    }

    public void setSchoolgradeboundary3(String schoolGradeBoundary3) {
        this.schoolGradeBoundary3 = schoolGradeBoundary3;
    }

    public List<qm_Evaluation> getQm_evaluations() {
        return qm_evaluations;
    }

    public void addQm_evaluation(Qm_evaluation qm_evaluation) {
        this.qm_evaluations.add(qm_evaluation);
    }
    public List<qm_Tag> getQm_tags() {
        return qm_tags;
    }

    public void addQm_tag(Qm_tag qm_tag) {
        this.qm_tags.add(qm_tag);
    }
    public qm_Evaluation getQm_evaluation() {
        return qm_evaluation;
    }

    public void setQm_evaluation(qm_Evaluation qm_evaluation) {
        this.qm_evaluation = qm_evaluation;
    }
    public List<qm_QualityModel> getQm_qualitymodels() {
        return qm_qualitymodels;
    }

    public void addQm_qualitymodel(Qm_qualitymodel qm_qualitymodel) {
        this.qm_qualitymodels.add(qm_qualitymodel);
    }
    public List<qm_MeasurementMethod> getQm_measurementmethods() {
        return qm_measurementmethods;
    }

    public void addQm_measurementmethod(Qm_measurementmethod qm_measurementmethod) {
        this.qm_measurementmethods.add(qm_measurementmethod);
    }
    public List<qm_Source> getQm_sources() {
        return qm_sources;
    }

    public void addQm_source(Qm_source qm_source) {
        this.qm_sources.add(qm_source);
    }
    public qm_Source getQm_source() {
        return qm_source;
    }

    public void setQm_source(qm_Source qm_source) {
        this.qm_source = qm_source;
    }
    public qm_Entity getQm_entity() {
        return qm_entity;
    }

    public void setQm_entity(qm_Entity qm_entity) {
        this.qm_entity = qm_entity;
    }
    public List<qm_Tool> getQm_tools() {
        return qm_tools;
    }

    public void addQm_tool(Qm_tool qm_tool) {
        this.qm_tools.add(qm_tool);
    }
    public qm_MeasurementMethod getQm_measurementmethod() {
        return qm_measurementmethod;
    }

    public void setQm_measurementmethod(qm_MeasurementMethod qm_measurementmethod) {
        this.qm_measurementmethod = qm_measurementmethod;
    }
    public qm_Measure getQm_measure() {
        return qm_measure;
    }

    public void setQm_measure(qm_Measure qm_measure) {
        this.qm_measure = qm_measure;
    }
    public List<qm_Factor> getQm_factors() {
        return qm_factors;
    }

    public void addQm_factor(Qm_factor qm_factor) {
        this.qm_factors.add(qm_factor);
    }
    public List<qm_Measure> getQm_measures() {
        return qm_measures;
    }

    public void addQm_measure(Qm_measure qm_measure) {
        this.qm_measures.add(qm_measure);
    }
    public qm_Tool getQm_tool() {
        return qm_tool;
    }

    public void setQm_tool(qm_Tool qm_tool) {
        this.qm_tool = qm_tool;
    }
    public List<qm_Entity> getQm_entitys() {
        return qm_entitys;
    }

    public void addQm_entity(Qm_entity qm_entity) {
        this.qm_entitys.add(qm_entity);
    }
    public qm_Tag getQm_tag() {
        return qm_tag;
    }

    public void setQm_tag(qm_Tag qm_tag) {
        this.qm_tag = qm_tag;
    }
    public qm_Factor getQm_factor() {
        return qm_factor;
    }

    public void setQm_factor(qm_Factor qm_factor) {
        this.qm_factor = qm_factor;
    }

}