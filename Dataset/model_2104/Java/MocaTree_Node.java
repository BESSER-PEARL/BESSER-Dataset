





import java.util.List;
import java.util.ArrayList;

public class MocaTree_Node extends Text {

    private int stopIndex;
    private int startIndex;
    private int startLineIndex;
    private int stopLineIndex;





    private List<MocaTree_Text> mocatree_texts;




    private MocaTree_File mocatree_file;




    private MocaTree_File mocatree_file;




    private MocaTree_Text mocatree_text;




    private MocaTree_Attribute mocatree_attribute;




    private List<MocaTree_Attribute> mocatree_attributes;


    public MocaTree_Node(
        int stopIndex,        int startIndex,        int startLineIndex,        int stopLineIndex    ) {
        super(
        );
        this.stopIndex = stopIndex;
        this.startIndex = startIndex;
        this.startLineIndex = startLineIndex;
        this.stopLineIndex = stopLineIndex;
        this.mocatree_texts = new ArrayList<>();
        this.mocatree_attributes = new ArrayList<>();
    }

    public MocaTree_Node(
        int stopIndex,        int startIndex,        int startLineIndex,        int stopLineIndex        ArrayList<MocaTree_Text> mocatree_texts,        ArrayList<MocaTree_Attribute> mocatree_attributes    ) {
        this.stopIndex = stopIndex;
        this.startIndex = startIndex;
        this.startLineIndex = startLineIndex;
        this.stopLineIndex = stopLineIndex;
        this.mocatree_texts = mocatree_texts;
        this.mocatree_attributes = mocatree_attributes;
    }

    public int getStopindex() {
        return stopIndex;
    }

    public void setStopindex(int stopIndex) {
        this.stopIndex = stopIndex;
    }
    public int getStartindex() {
        return startIndex;
    }

    public void setStartindex(int startIndex) {
        this.startIndex = startIndex;
    }
    public int getStartlineindex() {
        return startLineIndex;
    }

    public void setStartlineindex(int startLineIndex) {
        this.startLineIndex = startLineIndex;
    }
    public int getStoplineindex() {
        return stopLineIndex;
    }

    public void setStoplineindex(int stopLineIndex) {
        this.stopLineIndex = stopLineIndex;
    }

    public List<MocaTree_Text> getMocatree_texts() {
        return mocatree_texts;
    }

    public void addMocatree_text(Mocatree_text mocatree_text) {
        this.mocatree_texts.add(mocatree_text);
    }
    public MocaTree_File getMocatree_file() {
        return mocatree_file;
    }

    public void setMocatree_file(MocaTree_File mocatree_file) {
        this.mocatree_file = mocatree_file;
    }
    public MocaTree_File getMocatree_file() {
        return mocatree_file;
    }

    public void setMocatree_file(MocaTree_File mocatree_file) {
        this.mocatree_file = mocatree_file;
    }
    public MocaTree_Text getMocatree_text() {
        return mocatree_text;
    }

    public void setMocatree_text(MocaTree_Text mocatree_text) {
        this.mocatree_text = mocatree_text;
    }
    public MocaTree_Attribute getMocatree_attribute() {
        return mocatree_attribute;
    }

    public void setMocatree_attribute(MocaTree_Attribute mocatree_attribute) {
        this.mocatree_attribute = mocatree_attribute;
    }
    public List<MocaTree_Attribute> getMocatree_attributes() {
        return mocatree_attributes;
    }

    public void addMocatree_attribute(Mocatree_attribute mocatree_attribute) {
        this.mocatree_attributes.add(mocatree_attribute);
    }

}