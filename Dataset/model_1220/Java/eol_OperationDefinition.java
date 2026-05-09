





import java.util.List;
import java.util.ArrayList;

public class eol_OperationDefinition  {






    private eol_FOLMethodCallExpression eol_folmethodcallexpression;




    private eol_EOLLibraryModule eol_eollibrarymodule;




    private List<eol_OperationDefinition> eol_operationdefinitions;


    public eol_OperationDefinition(
    ) {
        this.eol_operationdefinitions = new ArrayList<>();
    }

    public eol_OperationDefinition(
        ArrayList<eol_OperationDefinition> eol_operationdefinitions    ) {
        this.eol_operationdefinitions = eol_operationdefinitions;
    }


    public eol_FOLMethodCallExpression getEol_folmethodcallexpression() {
        return eol_folmethodcallexpression;
    }

    public void setEol_folmethodcallexpression(eol_FOLMethodCallExpression eol_folmethodcallexpression) {
        this.eol_folmethodcallexpression = eol_folmethodcallexpression;
    }
    public eol_EOLLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EOLLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
    }
    public List<eol_OperationDefinition> getEol_operationdefinitions() {
        return eol_operationdefinitions;
    }

    public void addEol_operationdefinition(Eol_operationdefinition eol_operationdefinition) {
        this.eol_operationdefinitions.add(eol_operationdefinition);
    }

}