





import java.util.List;
import java.util.ArrayList;

public class becontent_EntityField  {

    private boolean isSearchPresentationHead;
    private boolean isSearchPresentationBody;
    private boolean isTextSearch;
    private boolean isPresented;





    private becontent_Entity becontent_entity;


    public becontent_EntityField(
        boolean isSearchPresentationHead,        boolean isSearchPresentationBody,        boolean isTextSearch,        boolean isPresented    ) {
        this.isSearchPresentationHead = isSearchPresentationHead;
        this.isSearchPresentationBody = isSearchPresentationBody;
        this.isTextSearch = isTextSearch;
        this.isPresented = isPresented;
    }


    public boolean getIssearchpresentationhead() {
        return isSearchPresentationHead;
    }

    public void setIssearchpresentationhead(boolean isSearchPresentationHead) {
        this.isSearchPresentationHead = isSearchPresentationHead;
    }
    public boolean getIssearchpresentationbody() {
        return isSearchPresentationBody;
    }

    public void setIssearchpresentationbody(boolean isSearchPresentationBody) {
        this.isSearchPresentationBody = isSearchPresentationBody;
    }
    public boolean getIstextsearch() {
        return isTextSearch;
    }

    public void setIstextsearch(boolean isTextSearch) {
        this.isTextSearch = isTextSearch;
    }
    public boolean getIspresented() {
        return isPresented;
    }

    public void setIspresented(boolean isPresented) {
        this.isPresented = isPresented;
    }

    public becontent_Entity getBecontent_entity() {
        return becontent_entity;
    }

    public void setBecontent_entity(becontent_Entity becontent_entity) {
        this.becontent_entity = becontent_entity;
    }

}