





import java.util.List;
import java.util.ArrayList;

public class stylesheets_Theme  {

    private String id;
    private String icon;
    private String label;





    private List<stylesheets_StyleSheet> stylesheets_stylesheets;




    private stylesheets_WorkspaceThemes stylesheets_workspacethemes;


    public stylesheets_Theme(
        String id,        String icon,        String label    ) {
        this.id = id;
        this.icon = icon;
        this.label = label;
        this.stylesheets_stylesheets = new ArrayList<>();
    }

    public stylesheets_Theme(
        String id,        String icon,        String label        ArrayList<stylesheets_StyleSheet> stylesheets_stylesheets    ) {
        this.id = id;
        this.icon = icon;
        this.label = label;
        this.stylesheets_stylesheets = stylesheets_stylesheets;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<stylesheets_StyleSheet> getStylesheets_stylesheets() {
        return stylesheets_stylesheets;
    }

    public void addStylesheets_stylesheet(Stylesheets_stylesheet stylesheets_stylesheet) {
        this.stylesheets_stylesheets.add(stylesheets_stylesheet);
    }
    public stylesheets_WorkspaceThemes getStylesheets_workspacethemes() {
        return stylesheets_workspacethemes;
    }

    public void setStylesheets_workspacethemes(stylesheets_WorkspaceThemes stylesheets_workspacethemes) {
        this.stylesheets_workspacethemes = stylesheets_workspacethemes;
    }

}