





import java.util.List;
import java.util.ArrayList;

public class modelDsl_SimpleTypeCollection extends CollectionReturnType {

    private String type;





    private modelDsl_DefModelSimpleTypeCollectionVariable modeldsl_defmodelsimpletypecollectionvariable;


    public modelDsl_SimpleTypeCollection(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public modelDsl_DefModelSimpleTypeCollectionVariable getModeldsl_defmodelsimpletypecollectionvariable() {
        return modeldsl_defmodelsimpletypecollectionvariable;
    }

    public void setModeldsl_defmodelsimpletypecollectionvariable(modelDsl_DefModelSimpleTypeCollectionVariable modeldsl_defmodelsimpletypecollectionvariable) {
        this.modeldsl_defmodelsimpletypecollectionvariable = modeldsl_defmodelsimpletypecollectionvariable;
    }

}