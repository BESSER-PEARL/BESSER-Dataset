





import java.util.List;
import java.util.ArrayList;

public class siddhi_ConstantValue  {

    private String siv;





    private siddhi_StringValue siddhi_stringvalue;




    private siddhi_TimeValue siddhi_timevalue;


    public siddhi_ConstantValue(
        String siv    ) {
        this.siv = siv;
    }


    public String getSiv() {
        return siv;
    }

    public void setSiv(String siv) {
        this.siv = siv;
    }

    public siddhi_StringValue getSiddhi_stringvalue() {
        return siddhi_stringvalue;
    }

    public void setSiddhi_stringvalue(siddhi_StringValue siddhi_stringvalue) {
        this.siddhi_stringvalue = siddhi_stringvalue;
    }
    public siddhi_TimeValue getSiddhi_timevalue() {
        return siddhi_timevalue;
    }

    public void setSiddhi_timevalue(siddhi_TimeValue siddhi_timevalue) {
        this.siddhi_timevalue = siddhi_timevalue;
    }

}