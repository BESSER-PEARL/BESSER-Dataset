





import java.util.List;
import java.util.ArrayList;

public class atem_PassThroughHtml extends AbstractComponent, SectionElementType {

    private String dsl_Passthrough_html_text;



    public atem_PassThroughHtml(
        String dsl_Passthrough_html_text    ) {
        super(
        );
        this.dsl_Passthrough_html_text = dsl_Passthrough_html_text;
    }


    public String getDsl_passthrough_html_text() {
        return dsl_Passthrough_html_text;
    }

    public void setDsl_passthrough_html_text(String dsl_Passthrough_html_text) {
        this.dsl_Passthrough_html_text = dsl_Passthrough_html_text;
    }


}