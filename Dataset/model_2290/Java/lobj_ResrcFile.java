





import java.util.List;
import java.util.ArrayList;

public class lobj_ResrcFile extends LearningObject {

    private String file_tn;
    private int filesize;
    private String resrcHref;
    private String originalextension;
    private String file;





    private lobj_HypertextContent lobj_hypertextcontent;




    private List<lobj_HypertextContent> lobj_hypertextcontents;


    public lobj_ResrcFile(
        String file_tn,        int filesize,        String resrcHref,        String originalextension,        String file    ) {
        super(
        );
        this.file_tn = file_tn;
        this.filesize = filesize;
        this.resrcHref = resrcHref;
        this.originalextension = originalextension;
        this.file = file;
        this.lobj_hypertextcontents = new ArrayList<>();
    }

    public lobj_ResrcFile(
        String file_tn,        int filesize,        String resrcHref,        String originalextension,        String file        ArrayList<lobj_HypertextContent> lobj_hypertextcontents    ) {
        this.file_tn = file_tn;
        this.filesize = filesize;
        this.resrcHref = resrcHref;
        this.originalextension = originalextension;
        this.file = file;
        this.lobj_hypertextcontents = lobj_hypertextcontents;
    }

    public String getFile_tn() {
        return file_tn;
    }

    public void setFile_tn(String file_tn) {
        this.file_tn = file_tn;
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

    public lobj_HypertextContent getLobj_hypertextcontent() {
        return lobj_hypertextcontent;
    }

    public void setLobj_hypertextcontent(lobj_HypertextContent lobj_hypertextcontent) {
        this.lobj_hypertextcontent = lobj_hypertextcontent;
    }
    public List<lobj_HypertextContent> getLobj_hypertextcontents() {
        return lobj_hypertextcontents;
    }

    public void addLobj_hypertextcontent(Lobj_hypertextcontent lobj_hypertextcontent) {
        this.lobj_hypertextcontents.add(lobj_hypertextcontent);
    }

}