/**
 * ChartGPT API
 * The ChartGPT API is a REST API that generates insights from data based on natural language questions.
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { HttpFile } from '../http/http';

/**
* The usage of the request.
*/
export class ResponseUsage {
    /**
    * The number of tokens used for the request.
    */
    'tokens'?: number;

    static readonly discriminator: string | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "tokens",
            "baseName": "tokens",
            "type": "number",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ResponseUsage.attributeTypeMap;
    }

    public constructor() {
    }
}

