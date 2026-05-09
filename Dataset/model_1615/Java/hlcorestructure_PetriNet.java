





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_PetriNet  {

    private String id;
    private String type;





    private hlcorestructure_Declaration hlcorestructure_declaration;




    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private hlcorestructure_ToolInfo hlcorestructure_toolinfo;




    private List<hlcorestructure_Page> hlcorestructure_pages;




    private hlcorestructure_Page hlcorestructure_page;




    private List<hlcorestructure_Declaration> hlcorestructure_declarations;




    private hlcorestructure_Name hlcorestructure_name;




    private List<hlcorestructure_ToolInfo> hlcorestructure_toolinfos;




    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private hlcorestructure_Name hlcorestructure_name;


    public hlcorestructure_PetriNet(
        String id,        String type    ) {
        this.id = id;
        this.type = type;
        this.hlcorestructure_pages = new ArrayList<>();
        this.hlcorestructure_declarations = new ArrayList<>();
        this.hlcorestructure_toolinfos = new ArrayList<>();
    }

    public hlcorestructure_PetriNet(
        String id,        String type        ArrayList<hlcorestructure_Page> hlcorestructure_pages,        ArrayList<hlcorestructure_Declaration> hlcorestructure_declarations,        ArrayList<hlcorestructure_ToolInfo> hlcorestructure_toolinfos    ) {
        this.id = id;
        this.type = type;
        this.hlcorestructure_pages = hlcorestructure_pages;
        this.hlcorestructure_declarations = hlcorestructure_declarations;
        this.hlcorestructure_toolinfos = hlcorestructure_toolinfos;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public hlcorestructure_Declaration getHlcorestructure_declaration() {
        return hlcorestructure_declaration;
    }

    public void setHlcorestructure_declaration(hlcorestructure_Declaration hlcorestructure_declaration) {
        this.hlcorestructure_declaration = hlcorestructure_declaration;
    }
    public hlcorestructure_PetriNetDoc getHlcorestructure_petrinetdoc() {
        return hlcorestructure_petrinetdoc;
    }

    public void setHlcorestructure_petrinetdoc(hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc) {
        this.hlcorestructure_petrinetdoc = hlcorestructure_petrinetdoc;
    }
    public hlcorestructure_ToolInfo getHlcorestructure_toolinfo() {
        return hlcorestructure_toolinfo;
    }

    public void setHlcorestructure_toolinfo(hlcorestructure_ToolInfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfo = hlcorestructure_toolinfo;
    }
    public List<hlcorestructure_Page> getHlcorestructure_pages() {
        return hlcorestructure_pages;
    }

    public void addHlcorestructure_page(Hlcorestructure_page hlcorestructure_page) {
        this.hlcorestructure_pages.add(hlcorestructure_page);
    }
    public hlcorestructure_Page getHlcorestructure_page() {
        return hlcorestructure_page;
    }

    public void setHlcorestructure_page(hlcorestructure_Page hlcorestructure_page) {
        this.hlcorestructure_page = hlcorestructure_page;
    }
    public List<hlcorestructure_Declaration> getHlcorestructure_declarations() {
        return hlcorestructure_declarations;
    }

    public void addHlcorestructure_declaration(Hlcorestructure_declaration hlcorestructure_declaration) {
        this.hlcorestructure_declarations.add(hlcorestructure_declaration);
    }
    public hlcorestructure_Name getHlcorestructure_name() {
        return hlcorestructure_name;
    }

    public void setHlcorestructure_name(hlcorestructure_Name hlcorestructure_name) {
        this.hlcorestructure_name = hlcorestructure_name;
    }
    public List<hlcorestructure_ToolInfo> getHlcorestructure_toolinfos() {
        return hlcorestructure_toolinfos;
    }

    public void addHlcorestructure_toolinfo(Hlcorestructure_toolinfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfos.add(hlcorestructure_toolinfo);
    }
    public hlcorestructure_PetriNetDoc getHlcorestructure_petrinetdoc() {
        return hlcorestructure_petrinetdoc;
    }

    public void setHlcorestructure_petrinetdoc(hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc) {
        this.hlcorestructure_petrinetdoc = hlcorestructure_petrinetdoc;
    }
    public hlcorestructure_Name getHlcorestructure_name() {
        return hlcorestructure_name;
    }

    public void setHlcorestructure_name(hlcorestructure_Name hlcorestructure_name) {
        this.hlcorestructure_name = hlcorestructure_name;
    }

}