





import java.util.List;
import java.util.ArrayList;

public class domain_PopupCanvas extends DefaultCavas, CanvasFrame, MultiLangLabel, ViewPortHolder, Categorized, FlexFields {

    private boolean modal;



    public domain_PopupCanvas(
        boolean modal    ) {
        super(
        );
        this.modal = modal;
    }


    public boolean getModal() {
        return modal;
    }

    public void setModal(boolean modal) {
        this.modal = modal;
    }


}