def create_bentoml_cli():
    # pylint: disable=unused-variable

    _cli = create_bento_service_cli()

    return _cli


cli = create_bentoml_cli()

if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
