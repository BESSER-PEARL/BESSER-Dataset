





import java.util.List;
import java.util.ArrayList;

public class common_StringValue extends Modifiable {

    private String value;





    private common_StringValueList common_stringvaluelist;


    public common_StringValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public common_StringValueList getCommon_stringvaluelist() {
        return common_stringvaluelist;
    }

    public void setCommon_stringvaluelist(common_StringValueList common_stringvaluelist) {
        this.common_stringvaluelist = common_stringvaluelist;
    }

}