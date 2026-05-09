





import java.util.List;
import java.util.ArrayList;

public class cjsidl_listDef extends containerDef {

    private String countComment;
    private String minCount;
    private String maxCount;





    private cjsidl_typeDef cjsidl_typedef;


    public cjsidl_listDef(
        String countComment,        String minCount,        String maxCount    ) {
        super(
        );
        this.countComment = countComment;
        this.minCount = minCount;
        this.maxCount = maxCount;
    }


    public String getCountcomment() {
        return countComment;
    }

    public void setCountcomment(String countComment) {
        this.countComment = countComment;
    }
    public String getMincount() {
        return minCount;
    }

    public void setMincount(String minCount) {
        this.minCount = minCount;
    }
    public String getMaxcount() {
        return maxCount;
    }

    public void setMaxcount(String maxCount) {
        this.maxCount = maxCount;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }

}