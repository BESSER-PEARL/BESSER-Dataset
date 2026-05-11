





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgHeadedMessageField extends TrgMessageField {

    private String headerId;



    public jointPackage_CPL2SPL_TrgHeadedMessageField(
        String headerId    ) {
        super(
        );
        this.headerId = headerId;
    }


    public String getHeaderid() {
        return headerId;
    }

    public void setHeaderid(String headerId) {
        this.headerId = headerId;
    }


}