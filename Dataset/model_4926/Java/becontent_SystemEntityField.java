





import java.util.List;
import java.util.ArrayList;

public class becontent_SystemEntityField  {

    private boolean isSearchPresentationBody;
    private boolean isSearchPresentationHead;
    private boolean isTextSearch;
    private boolean isPresented;





    private becontent_SystemEntity becontent_systementity;


    public becontent_SystemEntityField(
        boolean isSearchPresentationBody,        boolean isSearchPresentationHead,        boolean isTextSearch,        boolean isPresented    ) {
        this.isSearchPresentationBody = isSearchPresentationBody;
        this.isSearchPresentationHead = isSearchPresentationHead;
        this.isTextSearch = isTextSearch;
        this.isPresented = isPresented;
    }


    public boolean getIssearchpresentationbody() {
        return isSearchPresentationBody;
    }

    public void setIssearchpresentationbody(boolean isSearchPresentationBody) {
        this.isSearchPresentationBody = isSearchPresentationBody;
    }
    public boolean getIssearchpresentationhead() {
        return isSearchPresentationHead;
    }

    public void setIssearchpresentationhead(boolean isSearchPresentationHead) {
        this.isSearchPresentationHead = isSearchPresentationHead;
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

    public becontent_SystemEntity getBecontent_systementity() {
        return becontent_systementity;
    }

    public void setBecontent_systementity(becontent_SystemEntity becontent_systementity) {
        this.becontent_systementity = becontent_systementity;
    }

}