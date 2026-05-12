





import java.util.List;
import java.util.ArrayList;

public class View_Renderer_Interface  {






    private List<View_View> view_views;


    public View_Renderer_Interface(
    ) {
        this.view_views = new ArrayList<>();
    }

    public View_Renderer_Interface(
        ArrayList<View_View> view_views    ) {
        this.view_views = view_views;
    }


    public List<View_View> getView_views() {
        return view_views;
    }

    public void addView_view(View_view view_view) {
        this.view_views.add(view_view);
    }

}