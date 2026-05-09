





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_PetriNet  {

    private String type;
    private String id;





    private hlcorestructure_Page hlcorestructure_page;




    private hlcorestructure_Name hlcorestructure_name;




    private hlcorestructure_ToolInfo hlcorestructure_toolinfo;




    private hlcorestructure_Declaration hlcorestructure_declaration;




    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc;




    private List<hlcorestructure_ToolInfo> hlcorestructure_toolinfos;




    private List<hlcorestructure_Declaration> hlcorestructure_declarations;




    private hlcorestructure_Name hlcorestructure_name;




    private List<hlcorestructure_Page> hlcorestructure_pages;


    public hlcorestructure_PetriNet(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
        this.hlcorestructure_toolinfos = new ArrayList<>();
        this.hlcorestructure_declarations = new ArrayList<>();
        this.hlcorestructure_pages = new ArrayList<>();
    }

    public hlcorestructure_PetriNet(
        String type,        String id        ArrayList<hlcorestructure_ToolInfo> hlcorestructure_toolinfos,        ArrayList<hlcorestructure_Declaration> hlcorestructure_declarations,        ArrayList<hlcorestructure_Page> hlcorestructure_pages    ) {
        this.type = type;
        this.id = id;
        this.hlcorestructure_toolinfos = hlcorestructure_toolinfos;
        this.hlcorestructure_declarations = hlcorestructure_declarations;
        this.hlcorestructure_pages = hlcorestructure_pages;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public hlcorestructure_Page getHlcorestructure_page() {
        return hlcorestructure_page;
    }

    public void setHlcorestructure_page(hlcorestructure_Page hlcorestructure_page) {
        this.hlcorestructure_page = hlcorestructure_page;
    }
    public hlcorestructure_Name getHlcorestructure_name() {
        return hlcorestructure_name;
    }

    public void setHlcorestructure_name(hlcorestructure_Name hlcorestructure_name) {
        this.hlcorestructure_name = hlcorestructure_name;
    }
    public hlcorestructure_ToolInfo getHlcorestructure_toolinfo() {
        return hlcorestructure_toolinfo;
    }

    public void setHlcorestructure_toolinfo(hlcorestructure_ToolInfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfo = hlcorestructure_toolinfo;
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
    public hlcorestructure_PetriNetDoc getHlcorestructure_petrinetdoc() {
        return hlcorestructure_petrinetdoc;
    }

    public void setHlcorestructure_petrinetdoc(hlcorestructure_PetriNetDoc hlcorestructure_petrinetdoc) {
        this.hlcorestructure_petrinetdoc = hlcorestructure_petrinetdoc;
    }
    public List<hlcorestructure_ToolInfo> getHlcorestructure_toolinfos() {
        return hlcorestructure_toolinfos;
    }

    public void addHlcorestructure_toolinfo(Hlcorestructure_toolinfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfos.add(hlcorestructure_toolinfo);
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
    public List<hlcorestructure_Page> getHlcorestructure_pages() {
        return hlcorestructure_pages;
    }

    public void addHlcorestructure_page(Hlcorestructure_page hlcorestructure_page) {
        this.hlcorestructure_pages.add(hlcorestructure_page);
    }

}