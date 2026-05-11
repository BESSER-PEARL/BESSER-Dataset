





import java.util.List;
import java.util.ArrayList;

public class ric_Document extends EventComponent {

    private boolean index;
    private String fileName;
    private String title;





    private List<ric_List> ric_lists;




    private List<ric_RichWidget> ric_richwidgets;




    private List<ric_Form> ric_forms;




    private ric_Form ric_form;




    private List<ric_LineBreak> ric_linebreaks;




    private ric_Link ric_link;


    public ric_Document(
        boolean index,        String fileName,        String title    ) {
        super(
        );
        this.index = index;
        this.fileName = fileName;
        this.title = title;
        this.ric_lists = new ArrayList<>();
        this.ric_richwidgets = new ArrayList<>();
        this.ric_forms = new ArrayList<>();
        this.ric_linebreaks = new ArrayList<>();
    }

    public ric_Document(
        boolean index,        String fileName,        String title        ArrayList<ric_List> ric_lists,        ArrayList<ric_RichWidget> ric_richwidgets,        ArrayList<ric_Form> ric_forms,        ArrayList<ric_LineBreak> ric_linebreaks    ) {
        this.index = index;
        this.fileName = fileName;
        this.title = title;
        this.ric_lists = ric_lists;
        this.ric_richwidgets = ric_richwidgets;
        this.ric_forms = ric_forms;
        this.ric_linebreaks = ric_linebreaks;
    }

    public boolean getIndex() {
        return index;
    }

    public void setIndex(boolean index) {
        this.index = index;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<ric_List> getRic_lists() {
        return ric_lists;
    }

    public void addRic_list(Ric_list ric_list) {
        this.ric_lists.add(ric_list);
    }
    public List<ric_RichWidget> getRic_richwidgets() {
        return ric_richwidgets;
    }

    public void addRic_richwidget(Ric_richwidget ric_richwidget) {
        this.ric_richwidgets.add(ric_richwidget);
    }
    public List<ric_Form> getRic_forms() {
        return ric_forms;
    }

    public void addRic_form(Ric_form ric_form) {
        this.ric_forms.add(ric_form);
    }
    public ric_Form getRic_form() {
        return ric_form;
    }

    public void setRic_form(ric_Form ric_form) {
        this.ric_form = ric_form;
    }
    public List<ric_LineBreak> getRic_linebreaks() {
        return ric_linebreaks;
    }

    public void addRic_linebreak(Ric_linebreak ric_linebreak) {
        this.ric_linebreaks.add(ric_linebreak);
    }
    public ric_Link getRic_link() {
        return ric_link;
    }

    public void setRic_link(ric_Link ric_link) {
        this.ric_link = ric_link;
    }

}