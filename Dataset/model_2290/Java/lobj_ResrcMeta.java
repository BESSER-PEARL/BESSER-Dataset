




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_ResrcMeta extends LearningObject {

    private LocalDate lastModified;
    private int height;
    private LocalDate creationDate;
    private int width;
    private String filename;
    private String description;
    private String keywords;
    private String title;
    private String parameters;





    private lobj_ResrcFile lobj_resrcfile;


    public lobj_ResrcMeta(
        LocalDate lastModified,        int height,        LocalDate creationDate,        int width,        String filename,        String description,        String keywords,        String title,        String parameters    ) {
        super(
        );
        this.lastModified = lastModified;
        this.height = height;
        this.creationDate = creationDate;
        this.width = width;
        this.filename = filename;
        this.description = description;
        this.keywords = keywords;
        this.title = title;
        this.parameters = parameters;
    }


    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public lobj_ResrcFile getLobj_resrcfile() {
        return lobj_resrcfile;
    }

    public void setLobj_resrcfile(lobj_ResrcFile lobj_resrcfile) {
        this.lobj_resrcfile = lobj_resrcfile;
    }

}