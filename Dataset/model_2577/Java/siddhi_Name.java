





import java.util.List;
import java.util.ArrayList;

public class siddhi_Name  {

    private String na;





    private siddhi_Annotation siddhi_annotation;




    private siddhi_StreamAlias siddhi_streamalias;




    private siddhi_MathInOperation siddhi_mathinoperation;




    private siddhi_Features siddhi_features;


    public siddhi_Name(
        String na    ) {
        this.na = na;
    }


    public String getNa() {
        return na;
    }

    public void setNa(String na) {
        this.na = na;
    }

    public siddhi_Annotation getSiddhi_annotation() {
        return siddhi_annotation;
    }

    public void setSiddhi_annotation(siddhi_Annotation siddhi_annotation) {
        this.siddhi_annotation = siddhi_annotation;
    }
    public siddhi_StreamAlias getSiddhi_streamalias() {
        return siddhi_streamalias;
    }

    public void setSiddhi_streamalias(siddhi_StreamAlias siddhi_streamalias) {
        this.siddhi_streamalias = siddhi_streamalias;
    }
    public siddhi_MathInOperation getSiddhi_mathinoperation() {
        return siddhi_mathinoperation;
    }

    public void setSiddhi_mathinoperation(siddhi_MathInOperation siddhi_mathinoperation) {
        this.siddhi_mathinoperation = siddhi_mathinoperation;
    }
    public siddhi_Features getSiddhi_features() {
        return siddhi_features;
    }

    public void setSiddhi_features(siddhi_Features siddhi_features) {
        this.siddhi_features = siddhi_features;
    }

}