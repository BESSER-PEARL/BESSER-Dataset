





import java.util.List;
import java.util.ArrayList;

public class DOT_Arc extends GraphElement {

    private String group;
    private boolean constraint;
    private boolean decorate;
    private String sameTail;
    private String sameHead;
    private int minlen;





    private List<DOT_Layer> dot_layers;




    private DOT_Nodelike dot_nodelike;




    private DOT_Layer dot_layer;




    private DOT_Nodelike dot_nodelike;




    private DOT_Nodelike dot_nodelike;




    private DOT_Nodelike dot_nodelike;




    private DOT_Nodelike dot_nodelike;




    private DOT_Nodelike dot_nodelike;


    public DOT_Arc(
        String group,        boolean constraint,        boolean decorate,        String sameTail,        String sameHead,        int minlen    ) {
        super(
        );
        this.group = group;
        this.constraint = constraint;
        this.decorate = decorate;
        this.sameTail = sameTail;
        this.sameHead = sameHead;
        this.minlen = minlen;
        this.dot_layers = new ArrayList<>();
    }

    public DOT_Arc(
        String group,        boolean constraint,        boolean decorate,        String sameTail,        String sameHead,        int minlen        ArrayList<DOT_Layer> dot_layers    ) {
        this.group = group;
        this.constraint = constraint;
        this.decorate = decorate;
        this.sameTail = sameTail;
        this.sameHead = sameHead;
        this.minlen = minlen;
        this.dot_layers = dot_layers;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public boolean getConstraint() {
        return constraint;
    }

    public void setConstraint(boolean constraint) {
        this.constraint = constraint;
    }
    public boolean getDecorate() {
        return decorate;
    }

    public void setDecorate(boolean decorate) {
        this.decorate = decorate;
    }
    public String getSametail() {
        return sameTail;
    }

    public void setSametail(String sameTail) {
        this.sameTail = sameTail;
    }
    public String getSamehead() {
        return sameHead;
    }

    public void setSamehead(String sameHead) {
        this.sameHead = sameHead;
    }
    public int getMinlen() {
        return minlen;
    }

    public void setMinlen(int minlen) {
        this.minlen = minlen;
    }

    public List<DOT_Layer> getDot_layers() {
        return dot_layers;
    }

    public void addDot_layer(Dot_layer dot_layer) {
        this.dot_layers.add(dot_layer);
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public DOT_Layer getDot_layer() {
        return dot_layer;
    }

    public void setDot_layer(DOT_Layer dot_layer) {
        this.dot_layer = dot_layer;
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }

}