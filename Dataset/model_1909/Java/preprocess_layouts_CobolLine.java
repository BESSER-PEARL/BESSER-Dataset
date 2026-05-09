





import java.util.List;
import java.util.ArrayList;

public class preprocess_layouts_CobolLine  {

    private String sequenceArea;
    private String contentAreaB;
    private String indicatorArea;
    private String comment;
    private String contentAreaA;



    public preprocess_layouts_CobolLine(
        String sequenceArea,        String contentAreaB,        String indicatorArea,        String comment,        String contentAreaA    ) {
        this.sequenceArea = sequenceArea;
        this.contentAreaB = contentAreaB;
        this.indicatorArea = indicatorArea;
        this.comment = comment;
        this.contentAreaA = contentAreaA;
    }


    public String getSequencearea() {
        return sequenceArea;
    }

    public void setSequencearea(String sequenceArea) {
        this.sequenceArea = sequenceArea;
    }
    public String getContentareab() {
        return contentAreaB;
    }

    public void setContentareab(String contentAreaB) {
        this.contentAreaB = contentAreaB;
    }
    public String getIndicatorarea() {
        return indicatorArea;
    }

    public void setIndicatorarea(String indicatorArea) {
        this.indicatorArea = indicatorArea;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getContentareaa() {
        return contentAreaA;
    }

    public void setContentareaa(String contentAreaA) {
        this.contentAreaA = contentAreaA;
    }


}