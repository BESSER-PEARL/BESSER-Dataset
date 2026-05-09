





import java.util.List;
import java.util.ArrayList;

public class spem_Guidance extends MethodContentElement {

    private String attachment;





    private spem_BreakdownElement spem_breakdownelement;




    private spem_DescribableElement spem_describableelement;


    public spem_Guidance(
        String attachment    ) {
        super(
        );
        this.attachment = attachment;
    }


    public String getAttachment() {
        return attachment;
    }

    public void setAttachment(String attachment) {
        this.attachment = attachment;
    }

    public spem_BreakdownElement getSpem_breakdownelement() {
        return spem_breakdownelement;
    }

    public void setSpem_breakdownelement(spem_BreakdownElement spem_breakdownelement) {
        this.spem_breakdownelement = spem_breakdownelement;
    }
    public spem_DescribableElement getSpem_describableelement() {
        return spem_describableelement;
    }

    public void setSpem_describableelement(spem_DescribableElement spem_describableelement) {
        this.spem_describableelement = spem_describableelement;
    }

}