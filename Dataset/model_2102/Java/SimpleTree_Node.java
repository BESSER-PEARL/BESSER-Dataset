





import java.util.List;
import java.util.ArrayList;

public class SimpleTree_Node extends Text {

    private int stopLineIndex;
    private int stopIndex;
    private int startIndex;
    private int startLineIndex;





    private List<SimpleTree_Attribute> simpletree_attributes;




    private SimpleTree_Text simpletree_text;




    private List<SimpleTree_Text> simpletree_texts;




    private SimpleTree_Attribute simpletree_attribute;


    public SimpleTree_Node(
        int stopLineIndex,        int stopIndex,        int startIndex,        int startLineIndex    ) {
        super(
        );
        this.stopLineIndex = stopLineIndex;
        this.stopIndex = stopIndex;
        this.startIndex = startIndex;
        this.startLineIndex = startLineIndex;
        this.simpletree_attributes = new ArrayList<>();
        this.simpletree_texts = new ArrayList<>();
    }

    public SimpleTree_Node(
        int stopLineIndex,        int stopIndex,        int startIndex,        int startLineIndex        ArrayList<SimpleTree_Attribute> simpletree_attributes,        ArrayList<SimpleTree_Text> simpletree_texts    ) {
        this.stopLineIndex = stopLineIndex;
        this.stopIndex = stopIndex;
        this.startIndex = startIndex;
        this.startLineIndex = startLineIndex;
        this.simpletree_attributes = simpletree_attributes;
        this.simpletree_texts = simpletree_texts;
    }

    public int getStoplineindex() {
        return stopLineIndex;
    }

    public void setStoplineindex(int stopLineIndex) {
        this.stopLineIndex = stopLineIndex;
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

    public List<SimpleTree_Attribute> getSimpletree_attributes() {
        return simpletree_attributes;
    }

    public void addSimpletree_attribute(Simpletree_attribute simpletree_attribute) {
        this.simpletree_attributes.add(simpletree_attribute);
    }
    public SimpleTree_Text getSimpletree_text() {
        return simpletree_text;
    }

    public void setSimpletree_text(SimpleTree_Text simpletree_text) {
        this.simpletree_text = simpletree_text;
    }
    public List<SimpleTree_Text> getSimpletree_texts() {
        return simpletree_texts;
    }

    public void addSimpletree_text(Simpletree_text simpletree_text) {
        this.simpletree_texts.add(simpletree_text);
    }
    public SimpleTree_Attribute getSimpletree_attribute() {
        return simpletree_attribute;
    }

    public void setSimpletree_attribute(SimpleTree_Attribute simpletree_attribute) {
        this.simpletree_attribute = simpletree_attribute;
    }

}