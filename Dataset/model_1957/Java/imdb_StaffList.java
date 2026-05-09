




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class imdb_StaffList  {

    private String elementType;
    private String coverPhoto;
    private String elements;
    private String name;
    private LocalDate createdDate;



    public imdb_StaffList(
        String elementType,        String coverPhoto,        String elements,        String name,        LocalDate createdDate    ) {
        this.elementType = elementType;
        this.coverPhoto = coverPhoto;
        this.elements = elements;
        this.name = name;
        this.createdDate = createdDate;
    }


    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }
    public String getCoverphoto() {
        return coverPhoto;
    }

    public void setCoverphoto(String coverPhoto) {
        this.coverPhoto = coverPhoto;
    }
    public String getElements() {
        return elements;
    }

    public void setElements(String elements) {
        this.elements = elements;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(LocalDate createdDate) {
        this.createdDate = createdDate;
    }


}