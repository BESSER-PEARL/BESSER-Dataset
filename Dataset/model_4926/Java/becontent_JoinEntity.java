





import java.util.List;
import java.util.ArrayList;

public class becontent_JoinEntity  {

    private String _id_model;





    private becontent_JoinEntity becontent_joinentity;




    private becontent_Entity becontent_entity;




    private becontent_Content becontent_content;


    public becontent_JoinEntity(
        String _id_model    ) {
        this._id_model = _id_model;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }

    public becontent_JoinEntity getBecontent_joinentity() {
        return becontent_joinentity;
    }

    public void setBecontent_joinentity(becontent_JoinEntity becontent_joinentity) {
        this.becontent_joinentity = becontent_joinentity;
    }
    public becontent_Entity getBecontent_entity() {
        return becontent_entity;
    }

    public void setBecontent_entity(becontent_Entity becontent_entity) {
        this.becontent_entity = becontent_entity;
    }
    public becontent_Content getBecontent_content() {
        return becontent_content;
    }

    public void setBecontent_content(becontent_Content becontent_content) {
        this.becontent_content = becontent_content;
    }

}