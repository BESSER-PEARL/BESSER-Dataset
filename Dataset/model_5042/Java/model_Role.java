





import java.util.List;
import java.util.ArrayList;

public class model_Role extends IEntity {






    private model_User model_user;


    public model_Role(
    ) {
        super(
        );
    }



    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }

}