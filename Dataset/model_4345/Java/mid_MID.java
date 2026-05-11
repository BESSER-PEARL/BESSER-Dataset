





import java.util.List;
import java.util.ArrayList;

public class mid_MID  {

    private String level;





    private List<Operator> operators;




    private List<mid_Model> mid_models;




    private List<Editor> editors;




    private List<mid_EStringToExtendibleElementMap> mid_estringtoextendibleelementmaps;


    public mid_MID(
        String level    ) {
        this.level = level;
        this.operators = new ArrayList<>();
        this.mid_models = new ArrayList<>();
        this.editors = new ArrayList<>();
        this.mid_estringtoextendibleelementmaps = new ArrayList<>();
    }

    public mid_MID(
        String level        ArrayList<Operator> operators,        ArrayList<mid_Model> mid_models,        ArrayList<Editor> editors,        ArrayList<mid_EStringToExtendibleElementMap> mid_estringtoextendibleelementmaps    ) {
        this.level = level;
        this.operators = operators;
        this.mid_models = mid_models;
        this.editors = editors;
        this.mid_estringtoextendibleelementmaps = mid_estringtoextendibleelementmaps;
    }

    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public List<Operator> getOperators() {
        return operators;
    }

    public void addOperator(Operator operator) {
        this.operators.add(operator);
    }
    public List<mid_Model> getMid_models() {
        return mid_models;
    }

    public void addMid_model(Mid_model mid_model) {
        this.mid_models.add(mid_model);
    }
    public List<Editor> getEditors() {
        return editors;
    }

    public void addEditor(Editor editor) {
        this.editors.add(editor);
    }
    public List<mid_EStringToExtendibleElementMap> getMid_estringtoextendibleelementmaps() {
        return mid_estringtoextendibleelementmaps;
    }

    public void addMid_estringtoextendibleelementmap(Mid_estringtoextendibleelementmap mid_estringtoextendibleelementmap) {
        this.mid_estringtoextendibleelementmaps.add(mid_estringtoextendibleelementmap);
    }

}