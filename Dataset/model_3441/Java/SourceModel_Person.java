





import java.util.List;
import java.util.ArrayList;

public class SourceModel_Person  {

    private String age;





    private SourceModel_Person sourcemodel_person;




    private SourceModel_Container sourcemodel_container;


    public SourceModel_Person(
        String age    ) {
        this.age = age;
    }


    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public SourceModel_Person getSourcemodel_person() {
        return sourcemodel_person;
    }

    public void setSourcemodel_person(SourceModel_Person sourcemodel_person) {
        this.sourcemodel_person = sourcemodel_person;
    }
    public SourceModel_Container getSourcemodel_container() {
        return sourcemodel_container;
    }

    public void setSourcemodel_container(SourceModel_Container sourcemodel_container) {
        this.sourcemodel_container = sourcemodel_container;
    }

}