





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_MimeType  {

    private String extension;
    private String name;





    private mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache;




    private mancoosimm_MimeTypeHandler mancoosimm_mimetypehandler;




    private List<mancoosimm_MimeTypeHandler> mancoosimm_mimetypehandlers;




    private mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache;


    public mancoosimm_MimeType(
        String extension,        String name    ) {
        this.extension = extension;
        this.name = name;
        this.mancoosimm_mimetypehandlers = new ArrayList<>();
    }

    public mancoosimm_MimeType(
        String extension,        String name        ArrayList<mancoosimm_MimeTypeHandler> mancoosimm_mimetypehandlers    ) {
        this.extension = extension;
        this.name = name;
        this.mancoosimm_mimetypehandlers = mancoosimm_mimetypehandlers;
    }

    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mancoosimm_MimeTypeHandlerCache getMancoosimm_mimetypehandlercache() {
        return mancoosimm_mimetypehandlercache;
    }

    public void setMancoosimm_mimetypehandlercache(mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache) {
        this.mancoosimm_mimetypehandlercache = mancoosimm_mimetypehandlercache;
    }
    public mancoosimm_MimeTypeHandler getMancoosimm_mimetypehandler() {
        return mancoosimm_mimetypehandler;
    }

    public void setMancoosimm_mimetypehandler(mancoosimm_MimeTypeHandler mancoosimm_mimetypehandler) {
        this.mancoosimm_mimetypehandler = mancoosimm_mimetypehandler;
    }
    public List<mancoosimm_MimeTypeHandler> getMancoosimm_mimetypehandlers() {
        return mancoosimm_mimetypehandlers;
    }

    public void addMancoosimm_mimetypehandler(Mancoosimm_mimetypehandler mancoosimm_mimetypehandler) {
        this.mancoosimm_mimetypehandlers.add(mancoosimm_mimetypehandler);
    }
    public mancoosimm_MimeTypeHandlerCache getMancoosimm_mimetypehandlercache() {
        return mancoosimm_mimetypehandlercache;
    }

    public void setMancoosimm_mimetypehandlercache(mancoosimm_MimeTypeHandlerCache mancoosimm_mimetypehandlercache) {
        this.mancoosimm_mimetypehandlercache = mancoosimm_mimetypehandlercache;
    }

}