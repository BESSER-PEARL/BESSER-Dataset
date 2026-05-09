





import java.util.List;
import java.util.ArrayList;

public class atem_PassThroughPdf extends AbstractComponent, SectionElementType {

    private String dsl_Passthrough_pdf_text;



    public atem_PassThroughPdf(
        String dsl_Passthrough_pdf_text    ) {
        super(
        );
        this.dsl_Passthrough_pdf_text = dsl_Passthrough_pdf_text;
    }


    public String getDsl_passthrough_pdf_text() {
        return dsl_Passthrough_pdf_text;
    }

    public void setDsl_passthrough_pdf_text(String dsl_Passthrough_pdf_text) {
        this.dsl_Passthrough_pdf_text = dsl_Passthrough_pdf_text;
    }


}