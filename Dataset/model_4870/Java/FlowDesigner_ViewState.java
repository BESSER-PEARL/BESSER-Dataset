





import java.util.List;
import java.util.ArrayList;

public class FlowDesigner_ViewState extends NamedState {

    private String view;



    public FlowDesigner_ViewState(
        String view    ) {
        super(
        );
        this.view = view;
    }


    public String getView() {
        return view;
    }

    public void setView(String view) {
        this.view = view;
    }


}