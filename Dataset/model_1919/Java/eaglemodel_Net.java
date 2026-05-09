





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Net  {

    private String name;
    private int class_;





    private eaglemodel_Nets eaglemodel_nets;




    private List<eaglemodel_Segment> eaglemodel_segments;


    public eaglemodel_Net(
        String name,        int class_    ) {
        this.name = name;
        this.class_ = class_;
        this.eaglemodel_segments = new ArrayList<>();
    }

    public eaglemodel_Net(
        String name,        int class_        ArrayList<eaglemodel_Segment> eaglemodel_segments    ) {
        this.name = name;
        this.class_ = class_;
        this.eaglemodel_segments = eaglemodel_segments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getClass_() {
        return class_;
    }

    public void setClass_(int class_) {
        this.class_ = class_;
    }

    public eaglemodel_Nets getEaglemodel_nets() {
        return eaglemodel_nets;
    }

    public void setEaglemodel_nets(eaglemodel_Nets eaglemodel_nets) {
        this.eaglemodel_nets = eaglemodel_nets;
    }
    public List<eaglemodel_Segment> getEaglemodel_segments() {
        return eaglemodel_segments;
    }

    public void addEaglemodel_segment(Eaglemodel_segment eaglemodel_segment) {
        this.eaglemodel_segments.add(eaglemodel_segment);
    }

}