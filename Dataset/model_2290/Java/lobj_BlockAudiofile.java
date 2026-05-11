





import java.util.List;
import java.util.ArrayList;

public class lobj_BlockAudiofile extends LearningObject {

    private String originalextension;
    private String file;
    private int filesize;
    private String resrcHref;





    private lobj_HypertextContent lobj_hypertextcontent;


    public lobj_BlockAudiofile(
        String originalextension,        String file,        int filesize,        String resrcHref    ) {
        super(
        );
        this.originalextension = originalextension;
        this.file = file;
        this.filesize = filesize;
        this.resrcHref = resrcHref;
    }


    public String getOriginalextension() {
        return originalextension;
    }

    public void setOriginalextension(String originalextension) {
        this.originalextension = originalextension;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public int getFilesize() {
        return filesize;
    }

    public void setFilesize(int filesize) {
        this.filesize = filesize;
    }
    public String getResrchref() {
        return resrcHref;
    }

    public void setResrchref(String resrcHref) {
        this.resrcHref = resrcHref;
    }

    public lobj_HypertextContent getLobj_hypertextcontent() {
        return lobj_hypertextcontent;
    }

    public void setLobj_hypertextcontent(lobj_HypertextContent lobj_hypertextcontent) {
        this.lobj_hypertextcontent = lobj_hypertextcontent;
    }

}