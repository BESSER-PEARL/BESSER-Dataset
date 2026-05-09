





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_MimeType  {

    private String name;
    private String extension;





    private mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache;




    private List<mancoosimm_MimeTypeHandler> mancoosimm_mimetypehandlers;




    private mancoosimm_MimeTypeHandler mancoosimm_mimetypehandler;




    private mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache;


    public mancoosimm_MimeType(
        String name,        String extension    ) {
        this.name = name;
        this.extension = extension;
        this.mancoosimm_mimetypehandlers = new ArrayList<>();
    }

    public mancoosimm_MimeType(
        String name,        String extension        ArrayList<mancoosimm_MimeTypeHandler> mancoosimm_mimetypehandlers    ) {
        this.name = name;
        this.extension = extension;
        this.mancoosimm_mimetypehandlers = mancoosimm_mimetypehandlers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }

    public mancoosimm_MimeTypeHandlerCache getMancoosimm_mimetypehandlercache() {
        return mancoosimm_mimetypehandlercache;
    }

    public void setMancoosimm_mimetypehandlercache(mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache) {
        this.mancoosimm_mimetypehandlercache = mancoosimm_mimetypehandlercache;
    }
    public List<mancoosimm_MimeTypeHandler> getMancoosimm_mimetypehandlers() {
        return mancoosimm_mimetypehandlers;
    }

    public void addMancoosimm_mimetypehandler(Mancoosimm_mimetypehandler mancoosimm_mimetypehandler) {
        this.mancoosimm_mimetypehandlers.add(mancoosimm_mimetypehandler);
    }
    public mancoosimm_MimeTypeHandler getMancoosimm_mimetypehandler() {
        return mancoosimm_mimetypehandler;
    }

    public void setMancoosimm_mimetypehandler(mancoosimm_MimeTypeHandler mancoosimm_mimetypehandler) {
        this.mancoosimm_mimetypehandler = mancoosimm_mimetypehandler;
    }
    public mancoosimm_MimeTypeHandlerCache getMancoosimm_mimetypehandlercache() {
        return mancoosimm_mimetypehandlercache;
    }

    public void setMancoosimm_mimetypehandlercache(mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache) {
        this.mancoosimm_mimetypehandlercache = mancoosimm_mimetypehandlercache;
    }

}