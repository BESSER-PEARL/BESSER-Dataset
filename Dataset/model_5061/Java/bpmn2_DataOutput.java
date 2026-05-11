





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataOutput extends ItemAwareElement {

    private String name;
    private boolean isCollection;





    private bpmn2_OutputSet bpmn2_outputset;




    private bpmn2_OutputSet bpmn2_outputset;




    private List<bpmn2_OutputSet> bpmn2_outputsets;




    private List<bpmn2_OutputSet> bpmn2_outputsets;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private bpmn2_OutputSet bpmn2_outputset;




    private List<bpmn2_OutputSet> bpmn2_outputsets;


    public bpmn2_DataOutput(
        String name,        boolean isCollection    ) {
        super(
        );
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2_outputsets = new ArrayList<>();
        this.bpmn2_outputsets = new ArrayList<>();
        this.bpmn2_outputsets = new ArrayList<>();
    }

    public bpmn2_DataOutput(
        String name,        boolean isCollection        ArrayList<bpmn2_OutputSet> bpmn2_outputsets,        ArrayList<bpmn2_OutputSet> bpmn2_outputsets,        ArrayList<bpmn2_OutputSet> bpmn2_outputsets    ) {
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2_outputsets = bpmn2_outputsets;
        this.bpmn2_outputsets = bpmn2_outputsets;
        this.bpmn2_outputsets = bpmn2_outputsets;
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

    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
    }
    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }

}