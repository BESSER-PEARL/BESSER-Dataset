





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Function extends Standard, Element {






    private contentfwk_Function contentfwk_function;




    private contentfwk_Function contentfwk_function;




    private List<contentfwk_Function> contentfwk_functions;


    public contentfwk_Function(
    ) {
        super(
        );
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Function(
        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.contentfwk_functions = contentfwk_functions;
    }


    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }

}