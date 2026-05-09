





import java.util.List;
import java.util.ArrayList;

public class cjsidl_variantDef extends containerDef {

    private String maxCount;
    private String minCount;
    private String vtagComment;





    private cjsidl_typeDef cjsidl_typedef;


    public cjsidl_variantDef(
        String maxCount,        String minCount,        String vtagComment    ) {
        super(
        );
        this.maxCount = maxCount;
        this.minCount = minCount;
        this.vtagComment = vtagComment;
    }


    public String getMaxcount() {
        return maxCount;
    }

    public void setMaxcount(String maxCount) {
        this.maxCount = maxCount;
    }
    public String getMincount() {
        return minCount;
    }

    public void setMincount(String minCount) {
        this.minCount = minCount;
    }
    public String getVtagcomment() {
        return vtagComment;
    }

    public void setVtagcomment(String vtagComment) {
        this.vtagComment = vtagComment;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }

}