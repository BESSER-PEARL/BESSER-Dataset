





import java.util.List;
import java.util.ArrayList;

public class lobj_ResrcFiletype  {

    private String filetypeImageBif;
    private String filetypeExtension;
    private String id;
    private boolean applet;
    private boolean image;
    private String filetypeImageSmall;
    private String filetypeDesc;





    private lobj_ResrcFile lobj_resrcfile;




    private lobj_BlockAudiofile lobj_blockaudiofile;


    public lobj_ResrcFiletype(
        String filetypeImageBif,        String filetypeExtension,        String id,        boolean applet,        boolean image,        String filetypeImageSmall,        String filetypeDesc    ) {
        this.filetypeImageBif = filetypeImageBif;
        this.filetypeExtension = filetypeExtension;
        this.id = id;
        this.applet = applet;
        this.image = image;
        this.filetypeImageSmall = filetypeImageSmall;
        this.filetypeDesc = filetypeDesc;
    }


    public String getFiletypeimagebif() {
        return filetypeImageBif;
    }

    public void setFiletypeimagebif(String filetypeImageBif) {
        this.filetypeImageBif = filetypeImageBif;
    }
    public String getFiletypeextension() {
        return filetypeExtension;
    }

    public void setFiletypeextension(String filetypeExtension) {
        this.filetypeExtension = filetypeExtension;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getApplet() {
        return applet;
    }

    public void setApplet(boolean applet) {
        this.applet = applet;
    }
    public boolean getImage() {
        return image;
    }

    public void setImage(boolean image) {
        this.image = image;
    }
    public String getFiletypeimagesmall() {
        return filetypeImageSmall;
    }

    public void setFiletypeimagesmall(String filetypeImageSmall) {
        this.filetypeImageSmall = filetypeImageSmall;
    }
    public String getFiletypedesc() {
        return filetypeDesc;
    }

    public void setFiletypedesc(String filetypeDesc) {
        this.filetypeDesc = filetypeDesc;
    }

    public lobj_ResrcFile getLobj_resrcfile() {
        return lobj_resrcfile;
    }

    public void setLobj_resrcfile(lobj_ResrcFile lobj_resrcfile) {
        this.lobj_resrcfile = lobj_resrcfile;
    }
    public lobj_BlockAudiofile getLobj_blockaudiofile() {
        return lobj_blockaudiofile;
    }

    public void setLobj_blockaudiofile(lobj_BlockAudiofile lobj_blockaudiofile) {
        this.lobj_blockaudiofile = lobj_blockaudiofile;
    }

}