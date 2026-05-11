





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataInput extends ItemAwareElement {

    private String name;
    private boolean isCollection;





    private List<bpmn2_InputSet> bpmn2_inputsets;




    private bpmn2_ThrowEvent bpmn2_throwevent;




    private bpmn2_InputSet bpmn2_inputset;




    private bpmn2_InputSet bpmn2_inputset;




    private List<bpmn2_InputSet> bpmn2_inputsets;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private bpmn2_InputSet bpmn2_inputset;




    private List<bpmn2_InputSet> bpmn2_inputsets;


    public bpmn2_DataInput(
        String name,        boolean isCollection    ) {
        super(
        );
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2_inputsets = new ArrayList<>();
        this.bpmn2_inputsets = new ArrayList<>();
        this.bpmn2_inputsets = new ArrayList<>();
    }

    public bpmn2_DataInput(
        String name,        boolean isCollection        ArrayList<bpmn2_InputSet> bpmn2_inputsets,        ArrayList<bpmn2_InputSet> bpmn2_inputsets,        ArrayList<bpmn2_InputSet> bpmn2_inputsets    ) {
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2_inputsets = bpmn2_inputsets;
        this.bpmn2_inputsets = bpmn2_inputsets;
        this.bpmn2_inputsets = bpmn2_inputsets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }

    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }
    public bpmn2_ThrowEvent getBpmn2_throwevent() {
        return bpmn2_throwevent;
    }

    public void setBpmn2_throwevent(bpmn2_ThrowEvent bpmn2_throwevent) {
        this.bpmn2_throwevent = bpmn2_throwevent;
    }
    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }

}