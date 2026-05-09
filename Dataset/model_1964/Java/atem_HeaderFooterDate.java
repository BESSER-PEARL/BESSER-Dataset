





import java.util.List;
import java.util.ArrayList;

public class atem_HeaderFooterDate extends HeaderFooterFragment {

    private String dsl_HeaderFooterDate_Language;
    private boolean dsl_HeaderFooterDate;



    public atem_HeaderFooterDate(
        String dsl_HeaderFooterDate_Language,        boolean dsl_HeaderFooterDate    ) {
        super(
        );
        this.dsl_HeaderFooterDate_Language = dsl_HeaderFooterDate_Language;
        this.dsl_HeaderFooterDate = dsl_HeaderFooterDate;
    }


    public String getDsl_headerfooterdate_language() {
        return dsl_HeaderFooterDate_Language;
    }

    public void setDsl_headerfooterdate_language(String dsl_HeaderFooterDate_Language) {
        this.dsl_HeaderFooterDate_Language = dsl_HeaderFooterDate_Language;
    }
    public boolean getDsl_headerfooterdate() {
        return dsl_HeaderFooterDate;
    }

    public void setDsl_headerfooterdate(boolean dsl_HeaderFooterDate) {
        this.dsl_HeaderFooterDate = dsl_HeaderFooterDate;
    }


}