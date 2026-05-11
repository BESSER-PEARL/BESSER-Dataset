





import java.util.List;
import java.util.ArrayList;

public class contentfwk_BusinessArchitecture extends Architecture {






    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_BusinessService> contentfwk_businessservices;


    public contentfwk_BusinessArchitecture(
    ) {
        super(
        );
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_businessservices = new ArrayList<>();
    }

    public contentfwk_BusinessArchitecture(
        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_BusinessService> contentfwk_businessservices    ) {
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_businessservices = contentfwk_businessservices;
    }


    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_BusinessService> getContentfwk_businessservices() {
        return contentfwk_businessservices;
    }

    public void addContentfwk_businessservice(Contentfwk_businessservice contentfwk_businessservice) {
        this.contentfwk_businessservices.add(contentfwk_businessservice);
    }

}