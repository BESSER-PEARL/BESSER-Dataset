





import java.util.List;
import java.util.ArrayList;

public class bpmn2_OutputSet extends BaseElement {






    private bpmn2_InputOutputBinding bpmn2_inputoutputbinding;




    private bpmn2_InputSet bpmn2_inputset;




    private List<bpmn2_DataOutput> bpmn2_dataoutputs;




    private bpmn2_DataOutput bpmn2_dataoutput;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_InputSet> bpmn2_inputsets;




    private bpmn2_DataOutput bpmn2_dataoutput;




    private List<bpmn2_DataOutput> bpmn2_dataoutputs;




    private bpmn2_DataOutput bpmn2_dataoutput;




    private List<bpmn2_DataOutput> bpmn2_dataoutputs;




    private bpmn2_CatchEvent bpmn2_catchevent;


    public bpmn2_OutputSet(
    ) {
        super(
        );
        this.bpmn2_dataoutputs = new ArrayList<>();
        this.bpmn2_inputsets = new ArrayList<>();
        this.bpmn2_dataoutputs = new ArrayList<>();
        this.bpmn2_dataoutputs = new ArrayList<>();
    }

    public bpmn2_OutputSet(
        ArrayList<bpmn2_DataOutput> bpmn2_dataoutputs,        ArrayList<bpmn2_InputSet> bpmn2_inputsets,        ArrayList<bpmn2_DataOutput> bpmn2_dataoutputs,        ArrayList<bpmn2_DataOutput> bpmn2_dataoutputs    ) {
        this.bpmn2_dataoutputs = bpmn2_dataoutputs;
        this.bpmn2_inputsets = bpmn2_inputsets;
        this.bpmn2_dataoutputs = bpmn2_dataoutputs;
        this.bpmn2_dataoutputs = bpmn2_dataoutputs;
    }


    public bpmn2_InputOutputBinding getBpmn2_inputoutputbinding() {
        return bpmn2_inputoutputbinding;
    }

    public void setBpmn2_inputoutputbinding(bpmn2_InputOutputBinding bpmn2_inputoutputbinding) {
        this.bpmn2_inputoutputbinding = bpmn2_inputoutputbinding;
    }
    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public List<bpmn2_DataOutput> getBpmn2_dataoutputs() {
        return bpmn2_dataoutputs;
    }

    public void addBpmn2_dataoutput(Bpmn2_dataoutput bpmn2_dataoutput) {
        this.bpmn2_dataoutputs.add(bpmn2_dataoutput);
    }
    public bpmn2_DataOutput getBpmn2_dataoutput() {
        return bpmn2_dataoutput;
    }

    public void setBpmn2_dataoutput(bpmn2_DataOutput bpmn2_dataoutput) {
        this.bpmn2_dataoutput = bpmn2_dataoutput;
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }
    public bpmn2_DataOutput getBpmn2_dataoutput() {
        return bpmn2_dataoutput;
    }

    public void setBpmn2_dataoutput(bpmn2_DataOutput bpmn2_dataoutput) {
        this.bpmn2_dataoutput = bpmn2_dataoutput;
    }
    public List<bpmn2_DataOutput> getBpmn2_dataoutputs() {
        return bpmn2_dataoutputs;
    }

    public void addBpmn2_dataoutput(Bpmn2_dataoutput bpmn2_dataoutput) {
        this.bpmn2_dataoutputs.add(bpmn2_dataoutput);
    }
    public bpmn2_DataOutput getBpmn2_dataoutput() {
        return bpmn2_dataoutput;
    }

    public void setBpmn2_dataoutput(bpmn2_DataOutput bpmn2_dataoutput) {
        this.bpmn2_dataoutput = bpmn2_dataoutput;
    }
    public List<bpmn2_DataOutput> getBpmn2_dataoutputs() {
        return bpmn2_dataoutputs;
    }

    public void addBpmn2_dataoutput(Bpmn2_dataoutput bpmn2_dataoutput) {
        this.bpmn2_dataoutputs.add(bpmn2_dataoutput);
    }
    public bpmn2_CatchEvent getBpmn2_catchevent() {
        return bpmn2_catchevent;
    }

    public void setBpmn2_catchevent(bpmn2_CatchEvent bpmn2_catchevent) {
        this.bpmn2_catchevent = bpmn2_catchevent;
    }

}