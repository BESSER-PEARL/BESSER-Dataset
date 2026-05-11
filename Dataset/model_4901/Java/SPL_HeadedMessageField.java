





import java.util.List;
import java.util.ArrayList;

public class SPL_HeadedMessageField extends MessageField {

    private String headerId;



    public SPL_HeadedMessageField(
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