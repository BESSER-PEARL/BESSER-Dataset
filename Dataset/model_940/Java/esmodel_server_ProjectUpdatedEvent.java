





import java.util.List;
import java.util.ArrayList;

public class esmodel_server_ProjectUpdatedEvent extends ServerProjectEvent {






    private versioning_PrimaryVersionSpec versioning_primaryversionspec;


    public esmodel_server_ProjectUpdatedEvent(
    ) {
        super(
        );
    }



    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }

}